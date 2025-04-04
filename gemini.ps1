# GeminiAI.ps1
$env:GeminiKey = "AIzaSyD-qikvIHSzUI2gOZHzdsPOeI-7-QjX4l8"

function Invoke-GeminiAI {
    param(
        [Parameter(Mandatory)]
        [string]$UserInput
    )
    
    $API_KEY = $env:GeminiKey
    if (-not $API_KEY) {
        Write-Host "Please set your API key first:"
        $key = Read-Host "Enter API Key"
        $env:GeminiKey = $key
        $API_KEY = $key
    }

    $Headers = @{ 'Content-Type' = 'application/json' }

    $Instructions = @'
SYSTEM INSTRUCTIONS:
-Your goal is to provide ONLY code
-Codes should contain NO comments
-Do NOT include any additional text, besides important steps (only if necessary for setup)
'@

    $Body = @{ 
        contents = @( 
            @{ role = 'model'; parts = @( @{ text = $Instructions }) },
            @{ role = 'user'; parts = @( @{ text = $UserInput }) }
        )
    } | ConvertTo-Json -Depth 6

    $Url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=$API_KEY"

    try {
        $response = Invoke-RestMethod -Uri $Url -Method Post -Headers $Headers -Body $Body
        return $response.candidates[0].content.parts[0].text
    }
    catch {
        Write-Host "Error details:"
        Write-Host $_
        throw
    }
}

try {
    Write-Host "powershell >"
    $userPrompt = Read-Host
    Write-Host "Processing request..."
    $response = Invoke-GeminiAI -UserInput $userPrompt
    
    if ($response) {
        Write-Host "`nResponse:"
        Write-Host "-------------------"
        Write-Host $response
        Write-Host "-------------------"
        Write-Host "Press Enter to exit..."
        Read-Host | Out-Null
    }
}
catch {
    Write-Error "An error occurred: $_"
    Write-Host "Press Enter to exit..."
    Read-Host | Out-Null
}