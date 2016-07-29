import subprocess
import os
import stat

# testfile = "/home/andy/PycharmProjects/userswap_readfile_desy/testfile"
# st = os.stat(testfile)
# print oct(st.st_mode)

make_file_states = [True, False]

user_names = ["andytest", "andy"]

readable_for_everyone = [True, False]

for make_file in make_file_states:
    print "Make file?: ", make_file

    if make_file:
        for readable in readable_for_everyone:

            for user in user_names:
                # Make a file as a specific user
                command = 'sudo -u ' + user + ' bash -c \"echo "test" > testy_' + user + "\""
                print command
                proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                output, err = proc.communicate()
                proc.wait()
                print proc.returncode
                print "OUTPUT: ", output
                print "ERROR: ", err

                if not readable:
                    # Change the permissions so that only THAT user can READ the file
                    command = 'sudo -u ' + user + ' bash -c \'chmod 660 testy_' + user + "\'"
                    print command
                    proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                    output, err = proc.communicate()
                    proc.wait()
                    print proc.returncode
                    print "OUTPUT: ", output
                    print "ERROR: ", err

                else:
                    # Change the permissions so that EVERY user can READ the file
                    command = 'sudo -u ' + user + ' bash -c \'chmod 664 testy_' + user + "\'"
                    print command
                    proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                    output, err = proc.communicate()
                    proc.wait()
                    print proc.returncode
                    print "OUTPUT: ", output
                    print "ERROR: ", err

            print "Readable?: ", readable
            for user in user_names:
                print "USER:", user
                other_users = [users for users in user_names if users != user]
                for other_user in other_users:
                    print "OTHER:", other_user
                    command = 'sudo -u ' + user + ' bash -c \"cat testy_' + other_user + "\""
                    print command
                    proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                    output, err = proc.communicate()
                    proc.wait()
                    print proc.returncode
                    print "OUTPUT: ", output
                    print "ERROR: ", err
    else:
        for user in user_names:
            # Remove file just in case it was created before
            command = 'sudo -u ' + user + ' bash -c \"rm testy_' + user + "\""
            print command
            proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output, err = proc.communicate()
            proc.wait()
            print proc.returncode
            print "OUTPUT: ", output
            print "ERROR: ", err

            # Try to read file that doesn't exist (should fail)
            command = 'sudo -u ' + user + ' bash -c \"cat testy_' + user + "\""
            print command
            proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output, err = proc.communicate()
            proc.wait()
            print proc.returncode
            print "OUTPUT: ", output
            print "ERROR: ", err