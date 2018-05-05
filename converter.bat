%echo off
call pyuic4 -x gui_fajl.ui -o gui_fajl.py
call pyuic4 -x gui_about.ui -o gui_about.py
call pyuic4 -x gui_testic.ui -o gui_testic.py
call pyuic4 -x gui_glavni.ui -o gui_glavni.py
call pyrcc4 -py3 xx.qrc -o xx_rc.py