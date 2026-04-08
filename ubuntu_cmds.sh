# Firstly we create a directory named rover_mission using mkdir
mkdir rover_mission

# We move into it 
cd rover_mission

# Creates 3 empty files
touch log1.txt log2.txt log3.txt

# Renames log1.txt to mission_log.txt
mv log1.txt mission_log.txt

# Finds if there is any file with extension of .log in this directory
# Since i know the directory we wrote the name directly
find ~/rover_mission -type f -name "*.log"

# Displays the contents without opening the file
cat mission_log.txt

# Finds if there is a string with ERROR is present in it
grep 'ERROR' mission_log.txt

# Gives the word count of the file and -l makes it print without the filename
wc -l < mission_log.txt

#Gives all the time and date details
date

# Gives the cpu usage in real time
htop #Even top works

# Shutsdown the computer in 10 mins
# Using sudo so that no one else can shutdown the system
sudo shutdown +10
