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
def make_samples(dir):
    os.system(f"mkdir {dir}/samples")
    os.chdir("/Users/sandisk/Desktop/tmp/programming/cpp2")
    #making samples
    a_file = open("txt.json", "r")
    a_json = json.load(a_file)
    j = 1
    for i in a_json['tests']:
        os.chdir(f"{dir}/samples")
        in_file = open(f"sample{j}.in","w")
        out_file = open(f"sample{j}.out","w")
        in_file.write(i['input'])
        out_file.write(i['output'])
        j += 1
        os.chdir("/Users/sandisk/Desktop/tmp/programming/cpp2")
    #os.chdir(f"{dir}/samples")
    cpp_file_name = dir[-1:]
    os.system(f"cp /Users/sandisk/Desktop/tmp/programming/cpp2/main.cpp {dir}")
    os.system(f"mv {dir}/main.cpp {dir}/{cpp_file_name}.cpp")
    #print(list)

def create_files(dir):
    os.chdir(dir)
    os.system(f"cp /Users/sandisk/Desktop/tmp/programming/cpp2/Makefile {dir}")
    make_samples(dir)
    #os.chdir("/Users/sandisk/Desktop/tmp/programming/cpp2")
    os.chdir("/Users/sandisk")
    #create cpp file and use "main.cpp" as template file
    #print(os.getcwd())
    
def create_dir(arg_list,j):
    cur = os.getcwd()
    os.system(f"mkdir {cur}/{arg_list[j]}")
    create_files(f"{cur}/{arg_list[j]}")
        #print(f'dir {cur}/{arg_list[i]}')

#def make_prob(prob_count):
#    arg_list = sys.argv
#    create_dir(arg_list)

def download_problem_to_json(j):
    arg_list = sys.argv
    argument = '...'
    cur = os.getcwd()
    os.chdir("/Users/sandisk/Desktop"),os.chdir("tmp"),os.chdir("programming"),os.chdir("cpp2")
    main_proc = subprocess.Popen(['node index.js -> txt.json', '', argument], shell=True)
    time.sleep(5)# <-- There's no time.wait, but time.sleep.
    if os.stat("txt.json").st_size != 0:
        print("PROBLEM FOUND:")
        main_proc.terminate()
        proc1 = subprocess.Popen(['killall -9 node', '', argument], shell=True)
        pid = main_proc.pid # <--- access `pid` attribute to get the pid of the child process.
        pid1 = proc1.pid
        #for os proc double case so that it works without any exceptions/errors
        os.system("killall -9 node")
        print_json()
        print('KILLED NODE PROCESSES')
        print()
        os.chdir(cur)
        create_dir(arg_list,j)
        os.chdir("/Users/sandisk/Desktop"),os.chdir("tmp"),os.chdir("programming"),os.chdir("cpp2")
        #erase json
        open('txt.json', 'r+').truncate()
        os.chdir(cur)
        #os.chdir("/Users/sandisk")
        #DEBUG: print("kill successful")
        
def main():
    prob_count = int(sys.argv[1])
    #print(prob_count)
    
    #print(arg_list)
    #make_prob(prob_count)
    j = 2
    for i in range(prob_count):
       download_problem_to_json(j)
       j += 1
    #print(arg_list[0])

if __name__ == '__main__':
    main()
    str = "Hello World"
    print(str[-1:])
#TODO: reorganize and recreate makefile,integrate using OOP?,add helpbar if you are stuck on how to use, use try and except for download_json
