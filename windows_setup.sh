#!/bin/bash
set -euo pipefail

echo "[AEGIS-SENTINEL] Initializing Windows deployment sequence..."

echo "[*] Installing Python Telemetry & AI Dependencies..."
pip install fastapi uvicorn playwright

echo "[*] Installing Playwright Chromium Engine for Shadow-Apply..."
playwright install chromium

echo "[*] Verifying Deno API Bridge Requirements..."
if ! command -v deno &> /dev/null; then
    echo "[!] Deno not found. Please run 'irm https://deno.land/install.ps1 | iex' in Admin PowerShell."
else
    echo "[+] Deno environment verified."
fi

echo "[AEGIS-SENTINEL] Deployment foundation configured. Environment is ready to launch."
