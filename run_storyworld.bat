@echo off
echo 🌍 Running Storyworld Script...

REM Navigate to this folder (wherever the .bat is)
cd /d %~dp0

REM Run the story builder
python init_storyworld.py

REM Add all changes to Git
echo 🌀 Staging files...
git add .

REM Commit changes with default message
echo 📝 Committing...
git commit -m "Auto update from storyworld script"

REM Push to GitHub
echo 🚀 Pushing to GitHub...
git push origin main

echo ✅ Done! Press any key to close...
pause >nul
