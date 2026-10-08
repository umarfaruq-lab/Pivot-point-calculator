#!/bin/bash
set -e

echo "===================================================="
echo " OWASP Secured Pivot Point Application Installer    "
echo "===================================================="

# Check for Docker
if ! command -v docker &> /dev/null; then
    echo "[!] Docker is not installed. Installing Docker..."
    curl -fsSL https://get.docker.com | sh
fi

# Check for Docker Compose
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "[!] Installing Docker Compose..."
    apt-get update && apt-get install -y docker-compose-plugin
fi

echo "[*] Generating random cryptographic secret key..."
export FLASK_SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")

echo "[*] Building and launching application containers..."
docker compose up -d --build

echo "[✓] Application successfully deployed!"
echo "[✓] Healthcheck endpoint: http://localhost/health"
echo "[✓] Pivot Calculator API: http://localhost/api/v1/calculate"
