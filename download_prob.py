import subprocess,time,os,json

def print_json():
    a_file = open("txt.json", "r")
    a_json = json.load(a_file)
    pretty_json = json.dumps(a_json)
    a_file.close()
    print(pretty_json)
def get_tests():
    a_file = open("txt.json", "r")
    a_json = json.load(a_file)
    for i in a_json['tests']:
        print(i)
#is there even a need of this? get_io_type()
def get_io_type():
    a_file = open("txt.json", "r")
    a_json = json.load(a_file)
    for i in a_json['input']:
        print(i)
    for i in a_json['output']:
        print(i)
def create_samples():
    return 0
def create_files():
    
    #TODO: create files and directories according to problems and use ecnerwala template
    return 0
def download_problem_to_json():
    argument = '...'
    os.chdir("/Users/sandisk/Desktop")
    os.chdir("tmp")
    os.chdir("programming")
    os.chdir("cpp2")
    main_proc = subprocess.Popen(['node index.js -> txt.json', '', argument], shell=True)
    time.sleep(5)# <-- There's no time.wait, but time.sleep.
    if os.stat("txt.json").st_size != 0:
        print("PROBLEM FOUND, KILLING PROCESS")
        main_proc.terminate()
        proc1 = subprocess.Popen(['killall -9 node', '', argument], shell=True)
        pid = main_proc.pid # <--- access `pid` attribute to get the pid of the child process.
        pid1 = proc1.pid
        #for os proc double case so that it works without any exceptions/errors
        os.system("killall -9 node")
        print('killed node processes')
        print_json()
        #get_all()
        print("\n")
        #erase json
        open('txt.json', 'r+').truncate()
        os.chdir("/Users/sandisk")
        #DEBUG: print("kill successful")

prob_count = int(input("How many problems are going to parse? "))
for i in range(prob_count):
    download_problem_to_json()

