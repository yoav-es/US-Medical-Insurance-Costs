param()
Write-Host \"Building Docker image...\"
docker compose build
Write-Host \"Running report service...\"
docker compose run --rm report
