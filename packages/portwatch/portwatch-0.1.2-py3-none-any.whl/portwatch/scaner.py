
import asyncio
import psutil
import platform
import subprocess
import socket
import threading
import time
import logging
from typing import Union, List, Dict, Any, Optional, Set, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from enum import Enum

from .utils import load_dev_ports, get_port_description

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ScanMethod(Enum):
    PSUTIL = "psutil"
    NETSTAT = "netstat"
    SS = "ss"  # Linux modern replacement for netstat
    LSOF = "lsof"  # Unix/Linux
    POWERSHELL = "powershell"  # Windows

@dataclass
class ConnectionInfo:
    """Enhanced connection information"""
    pid: Optional[int]
    port: int
    process_name: str
    status: str
    local_address: str
    protocol: str
    process_path: Optional[str] = None
    process_cmdline: Optional[str] = None
    connection_time: Optional[float] = None
    note: str = ""

class CrossPlatformScanner:
    """Cross-platform network connection scanner with multiple fallback methods"""
    
    def __init__(self):
        self.system = platform.system().lower()
        self.available_methods = self._detect_available_methods()
        self.executor = ThreadPoolExecutor(max_workers=4, thread_name_prefix="scanner")
        self.cache = {}
        self.cache_timeout = 2.0  # Cache results for 2 seconds
        self.last_scan_time = 0
        self._dev_ports_cache = None
        self._dev_ports_cache_time = 0
        
        logger.info(f"Scanner initialized for {self.system} with methods: {[m.value for m in self.available_methods]}")

    def _detect_available_methods(self) -> List[ScanMethod]:
        """Detect available scanning methods for the current platform"""
        methods = []
        
        # Platform-specific methods with correct priority
        if self.system == "darwin":  # macOS
            # macOS: lsof and netstat work best, psutil often fails
            logger.info("Detecting macOS scanning methods...")
            
            if self._test_command(["lsof", "-i", "-P", "-n"]):
                methods.append(ScanMethod.LSOF)
                logger.info("lsof is available")
            
            if self._test_command(["netstat", "-an", "-f", "inet"]):
                methods.append(ScanMethod.NETSTAT)
                logger.info("netstat is available")
            
            # Try psutil last on macOS
            try:
                psutil.net_connections(kind='inet')
                methods.append(ScanMethod.PSUTIL)
                logger.info("psutil is available")
            except (psutil.AccessDenied, AttributeError, NotImplementedError) as e:
                logger.warning(f"psutil not available on macOS: {e}")
                
        elif self.system == "linux":
            # Linux: try ss, netstat, lsof, then psutil
            logger.info("Detecting Linux scanning methods...")
            
            if self._test_command(["ss", "-tuln"]):
                methods.append(ScanMethod.SS)
                logger.info("ss is available")
            
            if self._test_command(["netstat", "-tuln"]):
                methods.append(ScanMethod.NETSTAT)
                logger.info("netstat is available")
            
            if self._test_command(["lsof", "-i", "-P", "-n"]):
                methods.append(ScanMethod.LSOF)
                logger.info("lsof is available")
            
            try:
                psutil.net_connections(kind='inet')
                methods.append(ScanMethod.PSUTIL)
                logger.info("psutil is available")
            except (psutil.AccessDenied, AttributeError) as e:
                logger.warning(f"psutil not available: {e}")
                
        elif self.system == "windows":
            # Windows: psutil works best, then PowerShell, then netstat
            logger.info("Detecting Windows scanning methods...")
            
            try:
                psutil.net_connections()
                methods.append(ScanMethod.PSUTIL)
                logger.info("psutil is available")
            except (psutil.AccessDenied, AttributeError) as e:
                logger.warning(f"psutil not available: {e}")
            
            if self._test_command(["powershell", "-Command", "Get-NetTCPConnection | Select-Object -First 1"]):
                methods.append(ScanMethod.POWERSHELL)
                logger.info("PowerShell is available")
            
            if self._test_command(["netstat", "-ano"]):
                methods.append(ScanMethod.NETSTAT)
                logger.info("netstat is available")
        
        if not methods:
            logger.warning("No scanning methods available - will attempt emergency fallback")
            # Don't add PSUTIL here, let emergency fallback handle it
            
        return methods

    def _test_command(self, cmd: List[str]) -> bool:
        """Test if a command is available and executable"""
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                timeout=5, 
                check=False
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
            return False

    def _get_cached_dev_ports(self) -> Set[int]:
        """Get cached dev ports to avoid repeated file I/O"""
        current_time = time.time()
        if (self._dev_ports_cache is None or 
            current_time - self._dev_ports_cache_time > 30):  # Cache for 30 seconds
            self._dev_ports_cache = set(load_dev_ports())
            self._dev_ports_cache_time = current_time
        return self._dev_ports_cache

    def check_for_conflict(self, port: int) -> bool:
        """Check if port conflicts with configured dev ports"""
        return port in self._get_cached_dev_ports()

    async def scan_ports(self, filter_str: Optional[str] = None) -> List[Dict[str, Any]]:
        """Main scanning method with fallbacks and caching"""
        # Check cache first
        cache_key = f"scan_{filter_str or 'all'}"
        current_time = time.time()
        
        if (cache_key in self.cache and 
            current_time - self.cache[cache_key]['timestamp'] < self.cache_timeout):
            logger.debug("Returning cached scan results")
            return self.cache[cache_key]['data']

        # Scan using available methods
        results = []
        scan_success = False
        
        for method in self.available_methods:
            try:
                logger.debug(f"Attempting scan with method: {method.value}")
                results = await self._scan_with_method(method, filter_str)
                scan_success = True
                logger.debug(f"Scan successful with {method.value}: {len(results)} connections")
                break
            except Exception as e:
                logger.warning(f"Scan method {method.value} failed: {e}")
                continue
        
        if not scan_success:
            logger.error("All scan methods failed, attempting emergency fallback")
            results = await self._emergency_fallback_scan(filter_str)

        # Process and enhance results
        processed_results = await self._process_scan_results(results, filter_str)
        
        # Cache results
        self.cache[cache_key] = {
            'data': processed_results,
            'timestamp': current_time
        }
        
        self.last_scan_time = current_time
        return processed_results

    async def _scan_with_method(self, method: ScanMethod, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using a specific method"""
        loop = asyncio.get_event_loop()
        
        if method == ScanMethod.PSUTIL:
            return await loop.run_in_executor(self.executor, self._scan_psutil, filter_str)
        elif method == ScanMethod.NETSTAT:
            return await loop.run_in_executor(self.executor, self._scan_netstat, filter_str)
        elif method == ScanMethod.SS:
            return await loop.run_in_executor(self.executor, self._scan_ss, filter_str)
        elif method == ScanMethod.LSOF:
            return await loop.run_in_executor(self.executor, self._scan_lsof, filter_str)
        elif method == ScanMethod.POWERSHELL:
            return await loop.run_in_executor(self.executor, self._scan_powershell, filter_str)
        else:
            raise ValueError(f"Unknown scan method: {method}")

    def _scan_psutil(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using psutil with enhanced error handling"""
        connections = []

        try:
            # On Linux, psutil requires root for full connection info
            # Try with 'all' first, then fall back to 'inet'
            connection_types = ['all', 'inet', 'inet4', 'inet6', 'tcp', 'tcp4', 'tcp6', 'udp', 'udp4', 'udp6']

            for conn_type in connection_types:
                try:
                    logger.debug(f"Trying psutil with kind='{conn_type}'")
                    conns_found = 0

                    for conn in psutil.net_connections(kind=conn_type):
                        if not conn.laddr or not hasattr(conn.laddr, 'port'):
                            continue

                        # Include all connection states, not just LISTEN
                        # This captures ESTABLISHED, TIME_WAIT, etc.
                        if self.system == 'linux' and hasattr(conn, 'status'):
                            # On Linux, include LISTEN and ESTABLISHED connections
                            if conn.status not in [psutil.CONN_LISTEN, psutil.CONN_ESTABLISHED]:
                                continue
                        elif self.system == 'windows' and hasattr(conn, 'status'):
                            # On Windows, include LISTEN connections
                            if conn.status not in [psutil.CONN_LISTEN]:
                                continue

                        connection_info = self._extract_psutil_info(conn)
                        if connection_info and self._matches_filter(connection_info, filter_str):
                            connections.append(connection_info)
                            conns_found += 1

                    logger.debug(f"psutil {conn_type} found {conns_found} connections")

                    # If we got results, continue to check other types too
                    # Don't break early - we want to capture all connection types

                except (psutil.AccessDenied, AttributeError, PermissionError) as e:
                    logger.debug(f"psutil {conn_type} not accessible: {e}")
                    continue
                except Exception as e:
                    logger.debug(f"psutil {conn_type} error: {e}")
                    continue

            if not connections:
                # psutil failed completely, raise to try next method
                raise PermissionError("psutil requires elevated permissions or is not working")

        except Exception as e:
            logger.error(f"psutil scan failed: {e}")
            raise

        return connections

    def _extract_psutil_info(self, conn) -> Optional[ConnectionInfo]:
        """Extract connection information from psutil connection"""
        try:
            port = conn.laddr.port
            pid = conn.pid or 0
            status = conn.status or "UNKNOWN"
            local_addr = f"{conn.laddr.ip}:{conn.laddr.port}"
            protocol = "TCP" if hasattr(conn, 'type') and conn.type == socket.SOCK_STREAM else "UDP"
            
            process_name = ""
            process_path = None
            process_cmdline = None
            
            if pid and pid > 0:
                try:
                    process = psutil.Process(pid)
                    process_name = process.name()
                    try:
                        process_path = process.exe()
                        process_cmdline = ' '.join(process.cmdline()[:3])  # Limit cmdline length
                    except (psutil.AccessDenied, psutil.NoSuchProcess):
                        pass
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    process_name = f"PID:{pid}"
            
            return ConnectionInfo(
                pid=pid if pid > 0 else None,
                port=port,
                process_name=process_name,
                status=status,
                local_address=local_addr,
                protocol=protocol,
                process_path=process_path,
                process_cmdline=process_cmdline
            )
            
        except Exception as e:
            logger.debug(f"Failed to extract connection info: {e}")
            return None

    def _scan_netstat(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using netstat command"""
        connections = []
        
        try:
            if self.system == "windows":
                # Windows: scan both TCP and UDP
                for proto in ["TCP", "UDP"]:
                    cmd = ["netstat", "-ano", "-p", proto]
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                    if result.stdout:
                        connections.extend(self._parse_netstat_output(result.stdout, filter_str))
            elif self.system == "linux":
                # Linux: try with process info first, then without
                cmd = ["netstat", "-tulpn"]  # -p requires root but try anyway
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)

                # On Linux, netstat might fail without sudo, that's okay
                if result.returncode != 0:
                    logger.debug(f"netstat with -p failed, trying without process info")
                    cmd = ["netstat", "-tuln"]  # Without process info
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)

                if result.stdout:
                    connections.extend(self._parse_netstat_output(result.stdout, filter_str))
            else:  # macOS
                # macOS: scan both TCP and UDP
                for proto in ["tcp", "udp"]:
                    cmd = ["netstat", "-an", "-f", "inet", "-p", proto]
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                    if result.stdout:
                        connections.extend(self._parse_netstat_output(result.stdout, filter_str))

        except Exception as e:
            logger.error(f"netstat scan failed: {e}")
            raise

        return connections

    def _parse_netstat_output(self, output: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Parse netstat output across different platforms"""
        connections = []
        lines = output.strip().split('\n')
        
        for line in lines:
            try:
                parts = line.split()
                if len(parts) < 4:
                    continue
                
                # Skip header lines
                if any(header in line.lower() for header in ['proto', 'active', 'local', 'foreign', 'recv-q', 'send-q']):
                    continue
                
                protocol = parts[0].upper()
                if protocol not in ['TCP', 'TCP4', 'TCP6', 'UDP', 'UDP4', 'UDP6']:
                    continue
                
                # Normalize protocol name
                if protocol.startswith('TCP'):
                    protocol = 'TCP'
                elif protocol.startswith('UDP'):
                    protocol = 'UDP'
                
                # Parse differently for macOS vs Linux/Windows
                if self.system == "darwin":  # macOS format
                    # macOS netstat format: Proto Recv-Q Send-Q Local-Address Foreign-Address (state)
                    local_addr = parts[3] if len(parts) > 3 else ""
                    status = parts[5] if len(parts) > 5 else "UNKNOWN"
                else:  # Linux/Windows format
                    local_addr = parts[1] if len(parts) > 1 else ""
                    status = parts[3] if len(parts) > 3 else "UNKNOWN"
                
                # Extract port from address
                if not local_addr:
                    continue
                    
                # Handle different address formats: 
                # "127.0.0.1.8080" (macOS) or "127.0.0.1:8080" (Linux/Windows)
                # "*.*" or "*:*" (any address)
                port = None
                if '.' in local_addr and ':' not in local_addr:
                    # macOS format: IP.PORT
                    parts_addr = local_addr.rsplit('.', 1)
                    if len(parts_addr) == 2:
                        try:
                            port = int(parts_addr[1])
                        except ValueError:
                            continue
                elif ':' in local_addr:
                    # Standard format: IP:PORT or [IPv6]:PORT
                    port_str = local_addr.split(':')[-1]
                    try:
                        port = int(port_str)
                    except ValueError:
                        continue
                
                if not port:
                    continue
                
                # Include more connection states, not just LISTEN
                # This captures LISTEN, ESTABLISHED, TIME_WAIT, etc.
                if status.upper() not in ['LISTEN', 'LISTENING', 'BOUND', 'ESTABLISHED', 'TIME_WAIT']:
                    continue
                
                # Extract PID if available (Windows includes it)
                pid = None
                if len(parts) > 4 and self.system == "windows":
                    try:
                        pid = int(parts[4])
                    except ValueError:
                        pass
                
                connection_info = ConnectionInfo(
                    pid=pid,
                    port=port,
                    process_name="",
                    status=status,
                    local_address=local_addr,
                    protocol=protocol
                )
                
                # Try to get process info if we have PID
                if pid:
                    try:
                        process = psutil.Process(pid)
                        connection_info.process_name = process.name()
                    except:
                        connection_info.process_name = f"PID:{pid}"
                
                if self._matches_filter(connection_info, filter_str):
                    connections.append(connection_info)
                    
            except Exception as e:
                logger.debug(f"Failed to parse netstat line: '{line}' - {e}")
                continue
        
        return connections

    def _scan_ss(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using ss command (Linux)"""
        connections = []
        
        try:
            # Try with process info first
            cmd = ["ss", "-tulpn"]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            # If failed (likely permission issue), try without process info
            if result.returncode != 0 or not result.stdout.strip():
                logger.debug(f"ss with -p failed, trying without process info")
                cmd = ["ss", "-tuln"]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            if result.returncode != 0 and not result.stdout.strip():
                raise subprocess.CalledProcessError(result.returncode, cmd)
            
            connections = self._parse_ss_output(result.stdout, filter_str)
            
        except Exception as e:
            logger.error(f"ss scan failed: {e}")
            raise
        
        return connections

    def _parse_ss_output(self, output: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Parse ss command output"""
        connections = []
        lines = output.strip().split('\n')
        
        # Skip header lines
        start_index = 0
        for i, line in enumerate(lines):
            if any(header in line.lower() for header in ['netid', 'state', 'recv-q']):
                start_index = i + 1
                break
        
        for line in lines[start_index:]:
            if not line.strip():
                continue
                
            try:
                parts = line.split()
                if len(parts) < 5:
                    continue
                
                protocol = parts[0].upper() if parts[0] else "TCP"
                status = parts[1] if len(parts) > 1 else "UNKNOWN"
                
                # Find local address (varies by format)
                local_addr = ""
                for i, part in enumerate(parts):
                    if ':' in part and not part.startswith('['):
                        local_addr = part
                        break
                
                if not local_addr:
                    continue
                
                # Extract port
                if ':' in local_addr:
                    port_str = local_addr.split(':')[-1]
                    # Handle asterisks
                    if '*' in port_str:
                        continue
                    try:
                        port = int(port_str)
                    except ValueError:
                        continue
                else:
                    continue
                
                # Extract process info from last column (if available)
                process_name = ""
                pid = None
                
                # Look for process info in format: users:(("name",pid=123,fd=4))
                process_col = ' '.join(parts[5:]) if len(parts) > 5 else ""
                if 'users:' in process_col or 'pid=' in process_col:
                    try:
                        if 'pid=' in process_col:
                            pid_match = process_col.split('pid=')[1].split(',')[0].split(')')[0]
                            pid = int(pid_match)
                        
                        if '(("' in process_col:
                            name_match = process_col.split('(("')[1].split('"')[0]
                            process_name = name_match
                    except Exception as e:
                        logger.debug(f"Failed to parse process info from: {process_col} - {e}")
                
                connection_info = ConnectionInfo(
                    pid=pid,
                    port=port,
                    process_name=process_name or "",
                    status=status if status != "UNCONN" else "LISTEN",
                    local_address=local_addr,
                    protocol=protocol
                )
                
                if self._matches_filter(connection_info, filter_str):
                    connections.append(connection_info)
                    
            except Exception as e:
                logger.debug(f"Failed to parse ss line: '{line}' - {e}")
                continue
        
        return connections

    def _scan_lsof(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using lsof command (Unix/Linux/macOS)"""
        connections = []
        
        try:
            # lsof with various filter options
            # -i: network files
            # -P: no port name conversion
            # -n: no DNS resolution (faster)
            # -sTCP:LISTEN: only LISTEN state for TCP
            cmd = ["lsof", "-i", "-P", "-n"]
            
            # Add state filter if not already there (some systems might not support it)
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            
            # lsof might return non-zero but still have output
            if not result.stdout.strip():
                logger.warning(f"lsof returned no output, stderr: {result.stderr[:200]}")
                if result.returncode != 0:
                    raise subprocess.CalledProcessError(result.returncode, cmd)
            
            connections = self._parse_lsof_output(result.stdout, filter_str)
            
        except Exception as e:
            logger.error(f"lsof scan failed: {e}")
            raise
        
        return connections

    def _parse_lsof_output(self, output: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Parse lsof command output - works on macOS, Linux, BSD"""
        connections = []
        lines = output.strip().split('\n')
        
        # Find header line to determine column positions
        header_index = -1
        for i, line in enumerate(lines):
            if 'COMMAND' in line and 'PID' in line:
                header_index = i
                break
        
        if header_index == -1:
            logger.warning("Could not find lsof header line")
            start_index = 0
        else:
            start_index = header_index + 1
        
        for line in lines[start_index:]:
            if not line.strip():
                continue
            
            try:
                # lsof output varies, but generally:
                # COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
                parts = line.split(None, 8)  # Split on whitespace, max 9 parts
                
                if len(parts) < 9:
                    continue
                
                process_name = parts[0]
                
                try:
                    pid = int(parts[1])
                except ValueError:
                    continue
                
                # The NAME field (last column) contains the connection info
                name_field = parts[8]
                
                # NAME format examples:
                # "*:8080 (LISTEN)"
                # "localhost:3000 (LISTEN)"
                # "127.0.0.1:8080->192.168.1.1:54321 (ESTABLISHED)"
                # "[::1]:8080 (LISTEN)"
                
                # Extract protocol from TYPE field (parts[4])
                protocol = "TCP"
                type_field = parts[4] if len(parts) > 4 else ""
                if "UDP" in type_field.upper():
                    protocol = "UDP"
                elif "TCP" in type_field.upper() or "IPv" in type_field:
                    protocol = "TCP"
                
                # Parse the NAME field for port and status
                status = "UNKNOWN"
                if "(LISTEN)" in name_field:
                    status = "LISTEN"
                elif "(ESTABLISHED)" in name_field:
                    status = "ESTABLISHED"
                elif "(BOUND)" in name_field:
                    status = "LISTEN"
                
                # Include more connection states, not just LISTEN
                # This captures LISTEN, ESTABLISHED, TIME_WAIT, etc.
                if status not in ["LISTEN", "ESTABLISHED", "TIME_WAIT"]:
                    continue
                
                # Extract local address (before "->")
                local_addr = name_field.split('->')[0].split('(')[0].strip()
                
                # Extract port from various formats
                port = None
                
                # Try IPv6 format first: [::1]:8080
                if local_addr.startswith('['):
                    try:
                        port_part = local_addr.split(']:')[-1]
                        port = int(port_part)
                    except (ValueError, IndexError):
                        pass
                # Try IPv4/hostname format: *:8080 or localhost:8080 or 127.0.0.1:8080
                elif ':' in local_addr:
                    try:
                        port_part = local_addr.split(':')[-1]
                        port = int(port_part)
                    except ValueError:
                        pass
                # Try macOS alternative format: *.8080
                elif '.' in local_addr and local_addr.count('.') <= 4:
                    try:
                        parts_addr = local_addr.rsplit('.', 1)
                        if len(parts_addr) == 2:
                            port = int(parts_addr[1])
                    except ValueError:
                        pass
                
                if not port:
                    logger.debug(f"Could not extract port from lsof line: {name_field}")
                    continue
                
                connection_info = ConnectionInfo(
                    pid=pid,
                    port=port,
                    process_name=process_name,
                    status=status,
                    local_address=local_addr,
                    protocol=protocol
                )
                
                if self._matches_filter(connection_info, filter_str):
                    connections.append(connection_info)
                    
            except Exception as e:
                logger.debug(f"Failed to parse lsof line: '{line}' - {e}")
                continue
        
        logger.info(f"lsof parsed {len(connections)} connections")
        return connections

    def _scan_powershell(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using PowerShell on Windows"""
        connections = []
        
        try:
            # PowerShell command to get network connections with process info
            ps_cmd = """
            Get-NetTCPConnection | Where-Object {$_.State -eq 'Listen'} | 
            ForEach-Object {
                try {
                    $proc = Get-Process -Id $_.OwningProcess -ErrorAction Stop
                    "$($_.LocalAddress):$($_.LocalPort):$($_.OwningProcess):$($proc.ProcessName):TCP"
                } catch {
                    "$($_.LocalAddress):$($_.LocalPort):$($_.OwningProcess)::TCP"
                }
            }
            """
            
            result = subprocess.run(
                ["powershell", "-Command", ps_cmd],
                capture_output=True, text=True, timeout=15
            )
            
            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, ["powershell"])
            
            connections = self._parse_powershell_output(result.stdout, filter_str)
            
        except Exception as e:
            logger.error(f"PowerShell scan failed: {e}")
            raise
        
        return connections

    def _parse_powershell_output(self, output: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Parse PowerShell command output"""
        connections = []
        lines = output.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            try:
                parts = line.split(':')
                if len(parts) < 4:
                    continue
                
                local_ip = parts[0]
                port = int(parts[1])
                pid = int(parts[2]) if parts[2] else None
                process_name = parts[3] if len(parts) > 3 else ""
                protocol = parts[4] if len(parts) > 4 else "TCP"
                
                connection_info = ConnectionInfo(
                    pid=pid,
                    port=port,
                    process_name=process_name,
                    status="LISTEN",
                    local_address=f"{local_ip}:{port}",
                    protocol=protocol
                )
                
                if self._matches_filter(connection_info, filter_str):
                    connections.append(connection_info)
                    
            except Exception as e:
                logger.debug(f"Failed to parse PowerShell line: {line} - {e}")
                continue
        
        return connections

    def _matches_filter(self, connection: ConnectionInfo, filter_str: Optional[str]) -> bool:
        """Check if connection matches the filter string"""
        if not filter_str:
            return True
        
        filter_lower = filter_str.lower()
        return (
            filter_lower in connection.process_name.lower() or
            filter_lower in str(connection.port) or
            (connection.process_cmdline and filter_lower in connection.process_cmdline.lower())
        )

    async def _process_scan_results(self, connections: List[ConnectionInfo], filter_str: Optional[str]) -> List[Dict[str, Any]]:
        """Process and convert scan results to expected format"""
        results = []

        for conn in connections:
            # Skip invalid connections
            if not conn.port or conn.port <= 0:
                continue

            # Add conflict detection note
            note = ""
            if self.check_for_conflict(conn.port):
                note = get_port_description(conn.port)

            result = {
                "pid": conn.pid,
                "port": conn.port,
                "process_name": conn.process_name,
                "status": conn.status,
                "note": note,
                "protocol": getattr(conn, 'protocol', 'TCP'),
                "local_address": getattr(conn, 'local_address', f"*:{conn.port}")
            }

            # Add enhanced info if available
            if hasattr(conn, 'process_path') and conn.process_path:
                result["process_path"] = conn.process_path
            if hasattr(conn, 'process_cmdline') and conn.process_cmdline:
                result["process_cmdline"] = conn.process_cmdline

            results.append(result)

        # Remove duplicates based on port+pid+status combination to preserve different connection states
        unique_results = []
        seen = set()
        for result in results:
            key = (result["port"], result.get("pid"), result.get("status", ""))
            if key not in seen:
                seen.add(key)
                unique_results.append(result)

        # Sort by port number for consistent display
        unique_results.sort(key=lambda x: (x["port"], x.get("status", ""), x.get("pid") or 0))

        logger.debug(f"Processed {len(unique_results)} unique connections from {len(connections)} raw connections")
        return unique_results

    async def _emergency_fallback_scan(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Emergency fallback when all other methods fail"""
        logger.warning("Using emergency fallback scan method")
        connections = []

        try:
            # Multi-platform fallback approach
            if self.system == 'linux':
                # Linux: try /proc/net first
                logger.debug("Trying /proc/net/ method on Linux")
                connections.extend(await self._read_proc_net('tcp', filter_str))
                connections.extend(await self._read_proc_net('tcp6', filter_str))

            # Cross-platform socket probing for common ports
            if not connections:
                logger.debug("Trying socket probing fallback")
                connections.extend(await self._socket_probing_fallback(filter_str))

            # Try additional system-specific methods
            if not connections:
                if self.system == 'windows':
                    connections.extend(await self._windows_fallback_scan(filter_str))
                elif self.system in ['linux', 'darwin']:
                    connections.extend(await self._unix_fallback_scan(filter_str))

        except Exception as e:
            logger.error(f"Emergency fallback failed: {e}")

        logger.info(f"Emergency fallback found {len(connections)} connections")
        return connections

    async def _socket_probing_fallback(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Cross-platform socket probing fallback"""
        connections = []

        # Get ports to check
        dev_ports = list(self._get_cached_dev_ports())
        common_ports = [22, 80, 443, 3000, 3001, 3306, 5000, 5432, 8000, 8080, 9000, 27017, 6379, 9200]
        all_ports = list(set(dev_ports + common_ports))

        # Also check for running processes that might be using ports
        try:
            for proc in psutil.process_iter(['pid', 'name', 'connections']):
                try:
                    for conn in proc.connections():
                        if conn.status == 'LISTEN' and conn.laddr:
                            port = conn.laddr.port
                            if port not in all_ports:
                                all_ports.append(port)
                except (psutil.AccessDenied, psutil.NoSuchProcess):
                    continue
        except Exception as e:
            logger.debug(f"Could not get process connections: {e}")

        # Limit to reasonable number
        all_ports = sorted(list(set(all_ports)))[:50]

        async def check_port(port: int) -> Optional[ConnectionInfo]:
            try:
                # Try IPv4 first
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                result = sock.connect_ex(('127.0.0.1', port))
                sock.close()

                if result == 0:
                    return ConnectionInfo(
                        pid=None,
                        port=port,
                        process_name="Listening Service",
                        status="LISTEN",
                        local_address=f"127.0.0.1:{port}",
                        protocol="TCP"
                    )
            except Exception as e:
                logger.debug(f"Port {port} check failed: {e}")
            return None

        if all_ports:
            # Check ports concurrently but in smaller batches
            batch_size = 10
            for i in range(0, len(all_ports), batch_size):
                batch = all_ports[i:i + batch_size]
                tasks = [check_port(port) for port in batch]
                results = await asyncio.gather(*tasks, return_exceptions=True)

                for result in results:
                    if isinstance(result, ConnectionInfo):
                        if not filter_str or self._matches_filter(result, filter_str):
                            connections.append(result)

                # Small delay between batches
                await asyncio.sleep(0.01)

        return connections

    async def _windows_fallback_scan(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Windows-specific fallback using tasklist and netstat"""
        connections = []

        try:
            # Use tasklist to find processes with network connections
            result = subprocess.run(
                ['tasklist', '/v', '/fo', 'csv'],
                capture_output=True, text=True, timeout=10
            )

            if result.returncode == 0:
                # Parse tasklist output for processes that might be listening
                lines = result.stdout.strip().split('\n')
                for line in lines[1:]:  # Skip header
                    if 'LISTEN' in line.upper() or 'PORT' in line.upper():
                        # This is a basic approach - in practice you'd need more sophisticated parsing
                        pass

        except Exception as e:
            logger.debug(f"Windows fallback scan failed: {e}")

        return connections

    async def _unix_fallback_scan(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Unix-specific fallback methods"""
        connections = []

        try:
            # Try sockstat on FreeBSD/macOS
            if self.system == 'darwin':
                try:
                    result = subprocess.run(['sockstat'], capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        connections.extend(self._parse_sockstat_output(result.stdout, filter_str))
                except FileNotFoundError:
                    pass

            # Try fuser as last resort
            try:
                # Check if fuser is available
                result = subprocess.run(['fuser', '-V'], capture_output=True, timeout=2)
                if result.returncode == 0:
                    # Use fuser to find processes using common ports
                    for port in [80, 443, 3000, 8000, 8080, 22]:
                        try:
                            result = subprocess.run(['fuser', str(port) + '/tcp'],
                                                  capture_output=True, text=True, timeout=2)
                            if result.returncode == 0:
                                # Parse fuser output
                                pids = result.stdout.strip().split()
                                for pid in pids:
                                    try:
                                        pid_int = int(pid)
                                        proc = psutil.Process(pid_int)
                                        connections.append(ConnectionInfo(
                                            pid=pid_int,
                                            port=port,
                                            process_name=proc.name(),
                                            status="LISTEN",
                                            local_address=f"0.0.0.0:{port}",
                                            protocol="TCP"
                                        ))
                                    except (psutil.NoSuchProcess, ValueError):
                                        continue
                        except Exception:
                            continue
            except Exception:
                pass

        except Exception as e:
            logger.debug(f"Unix fallback scan failed: {e}")

        return connections

    def _parse_sockstat_output(self, output: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Parse sockstat output (FreeBSD/macOS)"""
        connections = []

        try:
            lines = output.strip().split('\n')
            for line in lines:
                if 'LISTEN' in line:
                    parts = line.split()
                    if len(parts) >= 5:
                        try:
                            port = int(parts[-1].split(':')[-1])
                            pid = int(parts[-2])
                            process_name = parts[0]

                            connection_info = ConnectionInfo(
                                pid=pid,
                                port=port,
                                process_name=process_name,
                                status="LISTEN",
                                local_address=f"0.0.0.0:{port}",
                                protocol="TCP"
                            )

                            if not filter_str or self._matches_filter(connection_info, filter_str):
                                connections.append(connection_info)

                        except (ValueError, IndexError):
                            continue

        except Exception as e:
            logger.debug(f"Failed to parse sockstat output: {e}")

        return connections
    
    async def _read_proc_net(self, protocol: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Read /proc/net/tcp or /proc/net/tcp6 directly (Linux only)"""
        connections = []
        
        try:
            proc_file = f"/proc/net/{protocol}"
            with open(proc_file, 'r') as f:
                lines = f.readlines()[1:]  # Skip header
            
            for line in lines:
                try:
                    parts = line.split()
                    if len(parts) < 10:
                        continue
                    
                    # Parse local address (format: "0100007F:1F90" = 127.0.0.1:8080)
                    local_addr_hex = parts[1]
                    if ':' not in local_addr_hex:
                        continue
                    
                    addr_hex, port_hex = local_addr_hex.split(':')
                    port = int(port_hex, 16)
                    
                    # Parse status (0A = LISTEN in hex)
                    status_hex = parts[3]
                    if status_hex != '0A':  # Only LISTEN connections
                        continue
                    
                    # Try to get PID from /proc
                    pid = None
                    inode = parts[9]
                    pid = self._find_pid_by_inode(inode)
                    
                    # Get process name if we have PID
                    process_name = ""
                    if pid:
                        try:
                            process = psutil.Process(pid)
                            process_name = process.name()
                        except:
                            process_name = f"PID:{pid}"
                    
                    connection_info = ConnectionInfo(
                        pid=pid,
                        port=port,
                        process_name=process_name,
                        status="LISTEN",
                        local_address=f"*:{port}",
                        protocol="TCP" if protocol.startswith('tcp') else "UDP"
                    )
                    
                    if not filter_str or self._matches_filter(connection_info, filter_str):
                        connections.append(connection_info)
                        
                except Exception as e:
                    logger.debug(f"Failed to parse /proc/net line: {line.strip()} - {e}")
                    continue
                    
        except Exception as e:
            logger.debug(f"Failed to read {proc_file}: {e}")
        
        return connections
    
    def _find_pid_by_inode(self, inode: str) -> Optional[int]:
        """Find PID by socket inode (Linux)"""
        try:
            import os
            import glob
            
            # Search /proc/*/fd/* for matching socket inode
            for pid_dir in glob.glob('/proc/[0-9]*'):
                try:
                    pid = int(os.path.basename(pid_dir))
                    fd_dir = os.path.join(pid_dir, 'fd')
                    
                    for fd in os.listdir(fd_dir):
                        try:
                            link = os.readlink(os.path.join(fd_dir, fd))
                            if f'socket:[{inode}]' in link:
                                return pid
                        except (OSError, PermissionError):
                            continue
                except (ValueError, PermissionError, FileNotFoundError):
                    continue
        except Exception as e:
            logger.debug(f"Failed to find PID for inode {inode}: {e}")
        
        return None

    def cleanup(self):
        """Cleanup scanner resources"""
        if hasattr(self, 'executor'):
            self.executor.shutdown(wait=True)

# Global scanner instance
_scanner: Optional[CrossPlatformScanner] = None

def get_scanner() -> CrossPlatformScanner:
    """Get or create the global scanner instance"""
    global _scanner
    if _scanner is None:
        _scanner = CrossPlatformScanner()
    return _scanner

# Backwards compatible functions
def check_for_conflict(port: int) -> bool:
    """Check if port conflicts with configured dev ports"""
    return get_scanner().check_for_conflict(port)

async def scan_ports(filter_str: Optional[str] = None) -> List[Dict[str, Any]]:
    """Main port scanning function with cross-platform support"""
    scanner = get_scanner()
    return await scanner.scan_ports(filter_str)

async def scan_changes(old_data: List[Dict[str, Any]], new_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Detect changes between scan results"""
    def _compute_changes():
        # Create comparison keys for more accurate change detection
        def make_key(item):
            return (item.get('port'), item.get('pid'), item.get('process_name'))
        
        old_keys = {make_key(item) for item in old_data}
        new_items = []
        
        for item in new_data:
            if make_key(item) not in old_keys:
                new_items.append(item)
        
        return new_items
    
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _compute_changes)

# Enhanced conflict checking with detailed process info
async def check_for_conflict_detailed(port: int) -> Optional[Dict[str, Any]]:
    """Get detailed conflict information for a port"""
    try:
        scanner = get_scanner()
        connections = await scanner.scan_ports()
        
        for conn in connections:
            if conn.get('port') == port:
                conflict_info = {
                    'port': port,
                    'pid': conn.get('pid'),
                    'process_name': conn.get('process_name', 'Unknown'),
                    'status': conn.get('status', 'Unknown'),
                    'is_conflict': scanner.check_for_conflict(port),
                    'description': get_port_description(port) if scanner.check_for_conflict(port) else None,
                    'protocol': conn.get('protocol', 'TCP'),
                    'local_address': conn.get('local_address', f'*:{port}')
                }
                
                if 'process_path' in conn:
                    conflict_info['process_path'] = conn['process_path']
                if 'process_cmdline' in conn:
                    conflict_info['process_cmdline'] = conn['process_cmdline']
                
                return conflict_info
        
        return None
    except Exception as e:
        logger.error(f"Detailed conflict check failed for port {port}: {e}")
        return None

# Cleanup function
def cleanup_scanner():
    """Cleanup scanner resources"""
    global _scanner
    if _scanner is not None:
        _scanner.cleanup()
        _scanner = None
        
        
        
#####
# Cleanup function
def cleanup_scanner():
    """Cleanup scanner resources"""
    global _scanner
    if _scanner is not None:
        _scanner.cleanup()
        _scanner = None

# Diagnostic functions for troubleshooting
async def diagnose_scanner() -> Dict[str, Any]:
    """Diagnose scanner capabilities and issues"""
    scanner = get_scanner()
    
    diagnosis = {
        'platform': platform.system(),
        'platform_version': platform.release(),
        'python_version': platform.python_version(),
        'available_methods': [m.value for m in scanner.available_methods],
        'tests': {}
    }
    
    # Test each method
    for method in scanner.available_methods:
        test_result = {'available': True, 'error': None, 'result_count': 0}
        
        try:
            results = await scanner._scan_with_method(method, None)
            test_result['result_count'] = len(results)
            if results:
                test_result['sample_ports'] = [r.port for r in results[:5]]
        except Exception as e:
            test_result['available'] = False
            test_result['error'] = str(e)[:200]
        
        diagnosis['tests'][method.value] = test_result
    
    # Check permissions
    diagnosis['permissions'] = {
        'can_read_proc_net': False,
        'can_use_psutil': False,
        'effective_uid': None,
        'is_root': False
    }
    
    try:
        import os
        if hasattr(os, 'geteuid'):
            uid = os.geteuid()
            diagnosis['permissions']['effective_uid'] = uid
            diagnosis['permissions']['is_root'] = (uid == 0)
        
        # Check /proc/net access on Linux
        if scanner.system == 'linux':
            try:
                with open('/proc/net/tcp', 'r') as f:
                    f.read(100)
                diagnosis['permissions']['can_read_proc_net'] = True
            except:
                pass
        
        # Check psutil
        try:
            conns = psutil.net_connections(kind='inet')
            diagnosis['permissions']['can_use_psutil'] = True
            diagnosis['permissions']['psutil_connection_count'] = len(conns)
        except Exception as e:
            diagnosis['permissions']['psutil_error'] = str(e)[:200]
            
    except Exception as e:
        diagnosis['permissions']['error'] = str(e)
    
    # Check command availability
    diagnosis['commands'] = {}
    commands_to_test = {
        'lsof': ['lsof', '-v'],
        'netstat': ['netstat', '--version'],
        'ss': ['ss', '--version']
    }
    
    for cmd_name, cmd in commands_to_test.items():
        try:
            result = subprocess.run(cmd, capture_output=True, timeout=2)
            diagnosis['commands'][cmd_name] = {
                'available': result.returncode == 0 or result.stdout or result.stderr,
                'path': subprocess.run(['which', cmd[0]], capture_output=True, text=True).stdout.strip()
            }
        except:
            diagnosis['commands'][cmd_name] = {'available': False}
    
    return diagnosis

async def test_scan_verbose() -> None:
    """Run a verbose test scan with detailed logging"""
    print("\n" + "="*60)
    print("     PortWatch Scanner Diagnostic")
    print("="*60 + "\n")
    
    # Run diagnosis
    diag = await diagnose_scanner()
    
    print(f"Platform: {diag['platform']} {diag['platform_version']}")
    print(f"Python: {diag['python_version']}")
    print(f"Available Methods: {', '.join(diag['available_methods']) if diag['available_methods'] else 'NONE'}\n")
    
    print("Method Test Results:")
    print("-" * 60)
    for method, result in diag['tests'].items():
        status = "✓ PASS" if result['available'] else "✗ FAIL"
        count = f"({result['result_count']} connections)" if result['available'] else ""
        print(f"  {method:15} {status:10} {count}")
        if result.get('error'):
            print(f"                Error: {result['error'][:80]}")
        if result.get('sample_ports'):
            print(f"                Sample ports: {result['sample_ports']}")
    
    print("\nPermissions:")
    print("-" * 60)
    perms = diag['permissions']
    print(f"  UID: {perms.get('effective_uid', 'N/A')}")
    print(f"  Root/Admin: {perms.get('is_root', False)}")
    print(f"  psutil works: {perms.get('can_use_psutil', False)}")
    if perms.get('psutil_error'):
        print(f"    psutil error: {perms['psutil_error'][:80]}")
    print(f"  /proc/net readable: {perms.get('can_read_proc_net', False)}")
    
    print("\nCommand Availability:")
    print("-" * 60)
    for cmd, info in diag.get('commands', {}).items():
        status = "✓" if info.get('available') else "✗"
        path = info.get('path', 'not found')
        print(f"  {cmd:10} {status}  {path}")
    
    print("\n" + "="*60)
    print("Running actual port scan...")
    print("="*60 + "\n")
    
    try:
        scanner = get_scanner()
        results = await scanner.scan_ports()
        
        if results:
            print(f"✓ Scan successful! Found {len(results)} listening ports:\n")
            for conn in sorted(results, key=lambda x: x['port'])[:20]:
                port = conn['port']
                proc = conn.get('process_name', 'Unknown')[:30]
                pid = conn.get('pid', 'N/A')
                status = conn.get('status', 'N/A')
                print(f"  Port {port:5}  PID: {str(pid):8}  Status: {status:10}  Process: {proc}")
            
            if len(results) > 20:
                print(f"\n  ... and {len(results) - 20} more")
        else:
            print("✗ Scan returned no results")
            print("\nTroubleshooting suggestions:")
            if diag['platform'] == 'Darwin':
                print("  macOS: Try running with 'sudo' for full process information")
                print("  Ensure Terminal/app has 'Full Disk Access' in System Preferences")
            elif diag['platform'] == 'Linux':
                print("  Linux: Try running with 'sudo' for full connection details")
                print("  Or use: sudo setcap cap_net_raw,cap_net_admin+eip /path/to/python")
            print("  Check that at least one method (lsof, netstat, ss) is available")
            
    except Exception as e:
        print(f"✗ Scan failed with error:\n  {e}")
        import traceback
        print("\nFull traceback:")
        traceback.print_exc()
    
    print("\n" + "="*60 + "\n")

# Add this convenience function to the module
async def quick_test():
    """Quick test of scanner functionality"""
    try:
        results = await scan_ports()
        print(f"Scanner working! Found {len(results)} listening ports")
        if results:
            for r in results[:5]:
                print(f"  Port {r['port']}: {r.get('process_name', 'Unknown')}")
        return True
    except Exception as e:
        print(f"Scanner failed: {e}")
        return False# scanner.py - Cross-platform optimized network scanner
