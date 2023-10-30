$exclude = @("venv", "BotChangeFormatNumber.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BotChangeFormatNumber.zip" -Force