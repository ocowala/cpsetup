import subprocess,time,os,json,sys
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

def create_files():

    return 0
def download_problem_to_json():
    argument = '...'
    cur = os.getcwd()
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
        print('KILLED NODE PROCESSES')
        print()
        print_json()
        print()
        #get_all()
        #erase json
        open('txt.json', 'r+').truncate()
        #os.chdir("/Users/sandisk")
        #DEBUG: print("kill successful")
        os.chdir(cur)
def main():
    prob_count = int(sys.argv[1])
    #print(prob_count)
    arg_list = sys.argv
    #print(arg_list)
    for i in range(prob_count):
       download_problem_to_json()
    #print(arg_list[0])

if __name__ == '__main__':
    main()
#TODO: create folders,input/output files ("sample.in","sample.out" [make separate ones for each testcase given by problem]) ,reorganize makefiles,integrate using OOP?
