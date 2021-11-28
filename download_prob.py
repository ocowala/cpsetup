import subprocess,time,os,json
def print_json():
    a_file = open("txt.json", "r")
    a_json = json.load(a_file)
    pretty_json = json.dumps(a_json, indent=4)
    a_file.close()
    print(pretty_json)
def parse_json():
    #TODO: parse json from json object
    return 0
def create_files():
    #TODO: create files and directories according to problems and use ecnerwala template
    return 0
def download_problem_to_json():
    argument = '...'
    proc = subprocess.Popen(['node index.js -> txt.json', '', argument], shell=True)
    time.sleep(10) # <-- There's no time.wait, but time.sleep.
    proc.terminate()
    print("kill all begin")
    #for shell proc
    proc1 = subprocess.Popen(['killall -9 node', '', argument], shell=True)
    print("kill all end")
    pid = proc.pid # <--- access `pid` attribute to get the pid of the child process.
    pid1 = proc1.pid
    #for os proc double case so that it works without any exceptions/errors
    os.system("killall -9 node")
    #print json
    print_json()
    print("\n\n")
    #erase json
    open('txt.json', 'r+').truncate()
    print("kill successful, copying info and creating relevant directories")
for i in range(3):
    download_problem_to_json()