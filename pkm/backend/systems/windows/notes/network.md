# 网络配置
---
## DHCP与手动切换

由于DHCP经常会给我们换IP，所以可以指定手动ip去固定。下边的脚本可以保存一些默认配置，运行时可以手动调试修改：

```powershell
# Set Manual IP Configuration
#Requires -RunAsAdministrator

# Default values
$defaultGateway = "10.15.1.1"
$primaryDNS = "10.15.1.1"
$secondaryDNS = "10.15.0.105"

# Get Ethernet adapter
$adapter = Get-NetAdapter -Name "Ethernet" -ErrorAction SilentlyContinue
if (-not $adapter) { 
    $adapter = Get-NetAdapter | Where-Object {$_.Status -eq "Up"} | Select-Object -First 1 
}

# Get current IP
$currentIP = (Get-NetIPAddress -InterfaceAlias $adapter.Name -AddressFamily IPv4 -ErrorAction SilentlyContinue).IPAddress
if (-not $currentIP) { $currentIP = "10.15.1.100" }

Write-Host "Adapter: $($adapter.Name)" -ForegroundColor Yellow
Write-Host "Current IP: $currentIP" -ForegroundColor Cyan
Write-Host ""

# Get user input
$ip = Read-Host "IP address [$currentIP]"
if (-not $ip) { $ip = $currentIP }

$gateway = Read-Host "Gateway [$defaultGateway]"
if (-not $gateway) { $gateway = $defaultGateway }

# Apply configuration
Write-Host "Applying configuration..." -ForegroundColor Yellow

# Set IP and gateway
netsh interface ip set address name="$($adapter.Name)" static $ip 255.255.0.0 $gateway

# Set two DNS servers
netsh interface ip set dns name="$($adapter.Name)" static $primaryDNS primary
netsh interface ip add dns name="$($adapter.Name)" $secondaryDNS index=2

# Show result
Write-Host "`nConfiguration applied successfully!" -ForegroundColor Green
Get-NetIPAddress -InterfaceAlias $adapter.Name -AddressFamily IPv4 | Select-Object IPAddress, PrefixLength
```

有时候别人的网络会把我们的ip顶掉，这就需要我们去重新dhcp一个新的ip，所以还需要从手动换回dhcp：

```powershell
# Switch to DHCP
#Requires -RunAsAdministrator

# Get Ethernet adapter
$adapter = Get-NetAdapter -Name "Ethernet" -ErrorAction SilentlyContinue
if (-not $adapter) { $adapter = Get-NetAdapter | Where-Object {$_.Status -eq "Up"} | Select-Object -First 1 }

Set-NetIPInterface -InterfaceAlias $adapter.Name -Dhcp Enabled
Set-DnsClientServerAddress -InterfaceAlias $adapter.Name -ResetServerAddresses
ipconfig /renew "$($adapter.Name)"

# Show IP
Get-NetIPAddress -InterfaceAlias $adapter.Name -AddressFamily IPv4 | Select-Object IPAddress
```

以上两个脚本都需要使用powershell的Admin模式。