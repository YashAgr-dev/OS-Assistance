from Speak import *
from commands import *
from commands.developer import *
from commands.files import *
from commands.windows import*
from commands.productivity import*
from commands.system import *
from commands.media import *
from commands.network import *
from commands.browser import *
from core import speak


def process_command(command, query):
    if command == "open chrome":
        speak("Opening Chrome")
        open_chrome()

#For Searching Files
    elif command == "search file":
        filename = input("Enter File Name : ")
        search_file(filename)  

#For Searching Folders
    elif command == "search folder":
        folder = input("Enter Folder Name : ")
        search_folder(folder)         

#For Creating Files
    elif command == "create file":
        filename = input("Enter File Name : ")
        create_file(filename)

#For Creating Folders
    elif command == "create folder":                    
        folder = input("Enter Folder Name : ")
        create_folder(folder)


#For Deleting Files
    elif command == "delete file":
        filename = input("Enter File Name : ")
        delete_file(filename)

#For Deleting Folders
    elif command == "delete folder":    
        folder = input("Enter Folder Name : ")
        delete_folder(folder)        

#For Renaming Files
    elif command == "rename file":                  
        old_name = input("Enter Old File Name : ")
        new_name = input("Enter New File Name : ")
        rename_file(old_name, new_name)


#For Copying Files
    elif command == "copy file":    
        source = input("Enter Source File Path : ")
        destination = input("Enter Destination File Path : ")
        copy_file(source, destination)


#For moving Files
    elif command == "move file":
        source = input("Enter Source File Path : ")
        destination = input("Enter Destination File Path : ")
        move_file(source, destination)


#For listing Files
    elif command == "list files":
        path = input("Enter Folder Path : ")
        list_files(path)    


#For Opening files
    elif command == "open file":
        file_path = input("Enter File Path : ")
        open_file(file_path)


#For Opening Folders
    elif command == "open folder":  
        folder_path = input("Enter Folder Path : ")
        open_folder(folder_path)

#For Zipping Folder
    elif command == "zip folder":
        folder = input("Folder Path : ")
        zip_name = input("ZIP Name : ")
        zip_folder(folder, zip_name)


#For Unzipping Folder
    elif command == "extract zip":
        zip_file = input("ZIP File Path : ")
        destination = input("Extract To : ")
        unzip_folder(zip_file, destination)


# ==============================
# Windows Automation Commands
# ==============================

    elif command == "open settings":
        open_settings()

    elif command == "open control panel":
        open_control_panel()

    elif command == "open task manager":
        open_task_manager()

    elif command == "open cmd":
        open_cmd()

    elif command == "open powershell":
        open_powershell()

    elif command == "open terminal":
        open_terminal()

    elif command == "open registry":
        open_registry()

    elif command == "open device manager":
        open_device_manager()

    elif command == "open disk management":
        open_disk_management()

    elif command == "open services":
        open_services()

    elif command == "open event viewer":
        open_event_viewer()

    elif command == "open system information":
        open_system_information()

    elif command == "open resource monitor":
        open_resource_monitor()

    elif command == "open performance monitor":
        open_performance_monitor()

    elif command == "open character map":
        open_character_map()

    elif command == "open snipping tool":
        open_snipping_tool()

    elif command == "open downloads":
        open_downloads()

    elif command == "open documents":
        open_documents()

    elif command == "open desktop":
        open_desktop()

    elif command == "open pictures":
        open_pictures()

    elif command == "open videos":
        open_videos()

    elif command == "open music":
        open_music()

    elif command == "open startup":
        open_startup()

    elif command == "open temp":
        open_temp()    

# ======================================
# Developer Assistant Commands
# ======================================

    elif command == "open vscode":
        open_vscode()

    elif command == "open cursor":
        open_cursor()

    elif command == "open android studio":
        open_android_studio()

    elif command == "open pycharm":
        open_pycharm()

    elif command == "open intellij":
        open_intellij()

    elif command == "open eclipse":
        open_eclipse()

    elif command == "open git bash":
        open_git_bash()

    elif command == "create python file":
        filename = input("File Name : ")
        create_python_file(filename)

    elif command == "create html file":
        filename = input("File Name : ")
        create_html_file(filename)

    elif command == "create css file":
        filename = input("File Name : ")
        create_css_file(filename)

    elif command == "create javascript file":
        filename = input("File Name : ")
        create_js_file(filename)

    elif command == "run python file":
        filename = input("Python File : ")
        run_python_file(filename)

    elif command == "run c file":
        filename = input("C File : ")
        run_c_file(filename)

    elif command == "run java file":
        filename = input("Java File : ")
        run_java_file(filename)

    elif command == "create virtual environment":
        name = input("Environment Name : ")
        create_virtual_environment(name)

    elif command == "activate virtual environment":
        name = input("Environment Name : ")
        activate_virtual_environment(name)

    elif command == "install package":
        package = input("Package Name : ")
        install_package(package)

    elif command == "uninstall package":
        package = input("Package Name : ")
        uninstall_package(package)

    elif command == "upgrade package":
        package = input("Package Name : ")
        upgrade_package(package)

    elif command == "freeze requirements":
        freeze_requirements()

    elif command == "open project":
        path = input("Project Path : ")
        open_project(path)

    elif command == "open folder in vscode":
        path = input("Folder Path : ")
        open_folder_vscode(path)

    elif command == "git init":
        git_init()

    elif command == "git status":
        git_status()

    elif command == "git add":
        git_add()

    elif command == "git commit":
        message = input("Commit Message : ")
        git_commit(message)

    elif command == "git push":
        git_push()

    elif command == "git pull":
        git_pull()

    elif command == "git clone":
        repo = input("Repository URL : ")
        git_clone(repo)

    elif command == "open localhost":
        open_localhost()

    elif command == "open github":
        open_github()

    elif command == "open stack overflow":
     open_stackoverflow()

    elif command == "open leetcode":
        open_leetcode()    

# ==========================================
# Git Automation Commands
# ==========================================

    elif command == "git init":
        git_init()

    elif command == "git status":
        git_status()

    elif command == "git add":
        git_add()

    elif command == "git add file":
        filename = input("Enter File Name: ")
        git_add_file(filename)

    elif command == "git commit":
        message = input("Commit Message: ")
        git_commit(message)

    elif command == "git push":
        git_push()

    elif command == "git pull":
        git_pull()

    elif command == "git clone":
        repository = input("Repository URL: ")
        git_clone(repository)

    elif command == "git branch":
        git_branch()

    elif command == "git checkout":
        branch = input("Branch Name: ")
        git_checkout(branch)

    elif command == "git create branch":
        branch = input("New Branch Name: ")
        git_create_branch(branch)

    elif command == "git delete branch":
        branch = input("Branch Name: ")
        git_delete_branch(branch)

    elif command == "git merge":
        branch = input("Branch Name: ")
        git_merge(branch)

    elif command == "git fetch":
        git_fetch()

    elif command == "git log":
            git_log()

    elif command == "git diff":
        git_diff()

    elif command == "git stash":
        git_stash()

    elif command == "git stash pop":
        git_stash_pop()

    elif command == "git reset":
        git_reset()

    elif command == "git remote":
        git_remote()

    elif command == "git add remote":
        name = input("Remote Name: ")
        url = input("Repository URL: ")
        git_add_remote(name, url)

    elif command == "git remove remote":
        name = input("Remote Name: ")
        git_remove_remote(name)

    elif command == "git tag":
        git_tag()

    elif command == "git create tag":
        tag = input("Tag Name: ")
        git_create_tag(tag)

    elif command == "git push tags":
        git_push_tags()

    elif command == "git version":
        git_version()   


# ======================================
# Developer Assistant Commands
# ======================================

    elif command == "open vscode":
        open_vscode()

    elif command == "open cursor":
        open_cursor()

    elif command == "open android studio":
        open_android_studio()

    elif command == "open pycharm":
        open_pycharm()

    elif command == "open intellij":
        open_intellij()

    elif command == "open eclipse":
        open_eclipse()

    elif command == "open git bash":
        open_git_bash()

    elif command == "create python file":
        filename = input("File Name : ")
        create_python_file(filename)

    elif command == "create html file":
        filename = input("File Name : ")
        create_html_file(filename)

    elif command == "create css file":
        filename = input("File Name : ")
        create_css_file(filename)

    elif command == "create javascript file":
        filename = input("File Name : ")
        create_js_file(filename)

    elif command == "run python file":
        filename = input("Python File : ")
        run_python_file(filename)

    elif command == "run c file":
        filename = input("C File : ")
        run_c_file(filename)

    elif command == "run java file":
        filename = input("Java File : ")
        run_java_file(filename)

    elif command == "create virtual environment":
        name = input("Environment Name : ")
        create_virtual_environment(name)

    elif command == "activate virtual environment":
        name = input("Environment Name : ")
        activate_virtual_environment(name)

    elif command == "install package":
        package = input("Package Name : ")
        install_package(package)

    elif command == "uninstall package":
        package = input("Package Name : ")
        uninstall_package(package)

    elif command == "upgrade package":
        package = input("Package Name : ")
        upgrade_package(package)

    elif command == "freeze requirements":
        freeze_requirements()

    elif command == "open project":
        path = input("Project Path : ")
        open_project(path)

    elif command == "open folder in vscode":
        path = input("Folder Path : ")
        open_folder_vscode(path)

    elif command == "git init":
        git_init()

    elif command == "git status":
        git_status()

    elif command == "git add":
        git_add()

    elif command == "git commit":
        message = input("Commit Message : ")
        git_commit(message)

    elif command == "git push":
        git_push()

    elif command == "git pull":
        git_pull()

    elif command == "git clone":
        repo = input("Repository URL : ")
        git_clone(repo)

    elif command == "open localhost":
        open_localhost()

    elif command == "open github":
        open_github()

    elif command == "open stack overflow":
        open_stackoverflow()

    elif command == "open leetcode":
        open_leetcode()     


# ==========================================
# Productivity Commands
# ==========================================

    elif command == "create note":

        note = input("Enter Note : ")

        create_note(note)

    elif command == "show notes":

        show_notes()

    elif command == "clear notes":

        clear_notes()

    elif command == "add task":

        task = input("Enter Task : ")

        add_task(task)

    elif command == "show tasks":

        show_tasks()

    elif command == "clear tasks":

        clear_tasks()

    elif command == "current date":

        current_date()

    elif command == "current time":

        current_time()

    elif command == "stopwatch":

        stopwatch()

    elif command == "countdown":

        seconds = int(input("Enter Seconds : "))

        countdown(seconds)

    elif command == "open calculator":

        open_calculator()

    elif command == "open notepad":

        open_notepad()

    elif command == "open clock":

        open_clock()

    elif command == "open calendar":

        open_calendar()

    elif command == "open paint":

        open_paint()

    elif command == "create quick folder":

        folder = input("Folder Name : ")

        quick_folder(folder)

    elif command == "open downloads":

        open_downloads()  

# ==========================================
# SYSTEM MONITOR
# ==========================================

    elif command == "cpu usage":
        cpu_usage()

    elif command == "cpu cores":
        cpu_cores()

    elif command == "cpu frequency":
        cpu_frequency()

    elif command == "ram usage":
        ram_usage()

    elif command == "swap memory":
        swap_memory()

    elif command == "disk usage":
        disk_usage()

    elif command == "disk partitions":
        disk_partitions()

    elif command == "battery percentage":
        battery_percentage()

    elif command == "battery status":
        battery_status()

    elif command == "boot time":
        boot_time()

    elif command == "system uptime":
        uptime()

    elif command == "system information":
        system_information()

    elif command == "live cpu":
        live_cpu()


    # ==========================================
# WINDOW CONTROL
# ==========================================

    elif command == "active window":
        active_window()

    elif command == "list windows":
        list_windows()

    elif command == "find window":
        title = input("Window Title : ")
        find_window(title)

    elif command == "maximize window":
        title = input("Window Title : ")
        maximize_window(title)

    elif command == "minimize window":
        title = input("Window Title : ")
        minimize_window(title)

    elif command == "restore window":
        title = input("Window Title : ")
        restore_window(title)

    elif command == "close window":
        title = input("Window Title : ")
        close_window(title)

    elif command == "activate window":
        title = input("Window Title : ")
        activate_window(title)

    elif command == "move window":
        title = input("Window Title : ")
        x = int(input("X Position : "))
        y = int(input("Y Position : "))
        move_window(title, x, y)

    elif command == "resize window":
        title = input("Window Title : ")
        width = int(input("Width : "))
        height = int(input("Height : "))
        resize_window(title, width, height)

    elif command == "show desktop":
        show_desktop()

    elif command == "lock windows":
        lock_windows()

    elif command == "switch window":
        switch_window()

    elif command == "window screenshot":
        filename = input("Screenshot Name : ")
        active_window_screenshot(filename) 


# ==========================================
# MEDIA CONTROL
# ==========================================

    elif command == "play":
        play_pause()

    elif command == "pause":
        play_pause()

    elif command == "play pause":
        play_pause()

    elif command == "next song":
        next_song()

    elif command == "previous song":
        previous_song()

    elif command == "stop media":
        stop_media()

    elif command == "volume up":
        volume_up()

    elif command == "volume down":
        volume_down()

    elif command == "mute":
        mute()

    elif command == "unmute":
        unmute()

    elif command == "brightness up":
        brightness_up()

    elif command == "brightness down":
        brightness_down()

    elif command == "set brightness":
        level = int(input("Brightness (0-100): "))
        set_brightness(level)

    elif command == "current brightness":
        current_brightness()

    elif command == "open spotify":
        open_spotify()

    elif command == "open vlc":
        open_vlc()

    elif command == "open media player":
        open_media_player()

    elif command == "open youtube music":
        open_youtube_music()

    elif command == "open spotify web":
        open_spotify_web()

    elif command == "maximum volume":
        volume_max()

    elif command == "minimum volume":
        volume_min()    

# ==========================================
# Browser Automation
# ==========================================

    elif command == "open chrome":
        open_chrome()

    elif command == "open edge":
        open_edge()

    elif command == "open firefox":
        open_firefox()

    elif command == "new tab":
        new_tab()

    elif command == "close tab":
        close_tab()

    elif command == "reopen tab":
        reopen_closed_tab()

    elif command == "next tab":
        next_tab()

    elif command == "previous tab":
        previous_tab()

    elif command == "new window":
        new_window()

    elif command == "incognito mode":
        incognito_mode()

    elif command == "refresh":
        refresh_page()

    elif command == "hard refresh":
        hard_refresh()

    elif command == "bookmark":
        bookmark_page()

    elif command == "history":
        open_history()

    elif command == "downloads":
        open_downloads()

    elif command == "open google":
        open_google()

    elif command == "open youtube":
        open_youtube()

    elif command == "open github":
        open_github()

    elif command == "open chatgpt":
        open_chatgpt()

    elif command == "open stack overflow":
        open_stackoverflow()

    elif command == "open leetcode":
        open_leetcode()

    elif command == "open gmail":
        open_gmail()

    elif command == "open drive":
        open_google_drive()

    elif command == "open maps":
        open_google_maps()

    elif command == "search google":
        query = input("Search : ")
        search_google(query)

    elif command == "search youtube":
        query = input("Search : ")
        search_youtube(query)

    elif command == "search github":
        query = input("Search : ")
        search_github(query)

    elif command == "search stack overflow":
        query = input("Search : ")
        search_stackoverflow(query)

    elif command == "search leetcode":
        query = input("Search : ")
        search_leetcode(query)

    elif command == "zoom in":
        zoom_in()

    elif command == "zoom out":
        zoom_out()

    elif command == "reset zoom":
        reset_zoom()

    elif command == "go back":
        go_back()

    elif command == "go forward":
        go_forward()

    elif command == "scroll up":
        scroll_up()

    elif command == "scroll down":
        scroll_down() 


# ==========================================
# NETWORK
# ==========================================

    elif command == "internet status":
        internet_status()

    elif command == "hostname":
        hostname()

    elif command == "local ip":
        local_ip()

    elif command == "public ip":
        public_ip()

    elif command == "mac address":
        mac_address()

    elif command == "network interfaces":
        network_interfaces()

    elif command == "network statistics":
        network_statistics()

    elif command == "active connections":
        active_connections()

    elif command == "dns servers":
        dns_servers()

    elif command == "default gateway":
        default_gateway()

    elif command == "adapter status":
        adapter_status()

    elif command == "ip config":
        ip_config()

    elif command == "routing table":
        routing_table()

    elif command == "arp table":
        arp_table()

    elif command == "network reset":
        network_reset()

    elif command == "network system":
        network_system()


# ==========================================
# WIFI MANAGEMENT
# ==========================================

    elif command == "wifi name":
        wifi_name()

    elif command == "saved wifi":
        saved_wifi_profiles()

    elif command == "wifi password":
        profile = input("Profile Name : ")
        wifi_password(profile)

    elif command == "scan wifi":
        scan_wifi()

    elif command == "connect wifi":
        profile = input("WiFi Profile : ")
        connect_wifi(profile)

    elif command == "disconnect wifi":
        disconnect_wifi()

    elif command == "delete wifi":
        profile = input("Profile Name : ")
        delete_wifi_profile(profile)

    elif command == "wifi signal":
        wifi_signal()

    elif command == "wifi channel":
        wifi_channel()

    elif command == "wifi radio":
        wifi_radio()

    elif command == "wifi security":
        profile = input("Profile Name : ")
        wifi_security(profile)

    elif command == "hotspot status":
        hotspot_status()

    elif command == "wifi driver":
        wifi_driver()

    elif command.startswith("open github"):
        query = command.replace("open github", "").strip()
        print(query)  # Debug
        open_github(query)

    #elif command.startswith("openchat gpt"):
        #query = command.replace("openchat gpt", "").strip()
       # print(query)  # Debug
       # open_chatgpt(query)
        
    elif command.startswith("search google"):
        query = command.replace("search google", "").strip()
        print(query)  # Debug
        search_google(query)

    elif command.startswith("search youtube"):
        query = command.replace("search youtube", "").strip()
        search_youtube(query)

    elif command == "open notepad":
        open_notepad()

    elif command == "open calculator":
        open_calculator()

    elif command == "open paint":
        open_paint()

    elif command == "open cmd":
        open_cmd()
        


    elif command == "open task manager":
        open_task_manager()

    elif command == "open control panel":
        open_control_panel()

    #elif command == "search file":
      #  filename = input("Enter file name: ")
     #   search_file(filename)

    elif command == "create folder":
        folder_name = input("Enter folder name: ")
        create_folder(folder_name)

    elif command == "delete file":
        file_name = input("Enter file name: ")
        delete_file(file_name)

    elif command == "rename file":
        old_name = input("Enter old file name: ")
        new_name = input("Enter new file name: ")
        rename_file(old_name, new_name)

    elif command == "list files":
        path = input("Enter folder path: ")
        list_files(path)


    elif command == "cpu usage":
        cpu_usage()

    elif command == "ram usage":
        ram_usage()

    elif command == "disk usage":
        disk_usage()    