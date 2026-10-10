Write-Host "==============================================" -ForegroundColor Cyan
Write-Host "   SUITE DE PRUEBAS CRUD - PRODUCT API (SOA)  " -ForegroundColor Cyan
Write-Host "==============================================" -ForegroundColor Cyan

$baseUrl = "http://127.0.0.1:8000/api/v1/products"

Write-Host "`n1. POST / (Crear Producto 1)..." -ForegroundColor Yellow
curl.exe -X POST "$baseUrl/" `
  -H "Content-Type: application/json" `
  -d "{\`"sku\`": \`"LAP-001\`", \`"name\`": \`"Laptop Gamer Pro\`", \`"price\`": 1500.00, \`"stock\`": 10}"

Write-Host "`n`n2. POST / (Crear Producto 2)..." -ForegroundColor Yellow
curl.exe -X POST "$baseUrl/" `
  -H "Content-Type: application/json" `
  -d "{\`"sku\`": \`"MOU-002\`", \`"name\`": \`"Mouse Inalámbrico\`", \`"price\`": 25.50, \`"stock\`": 50}"

Write-Host "`n`n3. GET / (Listar todos los productos con paginación)..." -ForegroundColor Yellow
curl.exe -X GET "$baseUrl/?skip=0&limit=10"

Write-Host "`n`n4. GET / (Filtrar por nombre 'Laptop')..." -ForegroundColor Yellow
curl.exe -X GET "$baseUrl/?name=Laptop"

Write-Host "`n`n5. GET /{id} (Consultar Producto con ID 1)..." -ForegroundColor Yellow
curl.exe -X GET "$baseUrl/1"

Write-Host "`n`n6. PUT /{id} (Reemplazo completo de Producto ID 1)..." -ForegroundColor Yellow
curl.exe -X PUT "$baseUrl/1" `
  -H "Content-Type: application/json" `
  -d "{\`"sku\`": \`"LAP-001\`", \`"name\`": \`"Laptop Gamer Ultra\`", \`"price\`": 1650.00, \`"stock\`": 8}"

Write-Host "`n`n7. PATCH /{id} (Actualización parcial de precio y stock)..." -ForegroundColor Yellow
curl.exe -X PATCH "$baseUrl/1" `
  -H "Content-Type: application/json" `
  -d "{\`"price\`": 1599.99, \`"stock\`": 12}"

Write-Host "`n`n8. DELETE /{id} (Eliminar Producto ID 2)..." -ForegroundColor Yellow
curl.exe -X DELETE "$baseUrl/2"

Write-Host "`n`n9. GET /{id} (Verificar que ID 2 fue eliminado - debe retornar 404)..." -ForegroundColor Yellow
curl.exe -X GET "$baseUrl/2"

Write-Host "`n`n==============================================" -ForegroundColor Green
Write-Host "         PRUEBAS COMPLETADAS CON ÉXITO        " -ForegroundColor Green
Write-Host "==============================================" -ForegroundColor Green