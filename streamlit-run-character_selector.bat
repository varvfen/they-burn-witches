@echo off
cd /d %~dp0



python character_selector.py






echo 🌐 Launching Streamlit app in browser...
start "" streamlit run character_selector.py

echo ✅ All done! Streamlit is now running in your browser.
pause
