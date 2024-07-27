# Interactly-task-Dhruvin
MongoDB Setup in Local in Windows
1. Install MongoDB Server, Shell and Compass
2. extract shell file into program files-mongodb
3. go to extracted file-bin and copy mongosh file (which is .exe file)
4. paste this file into the server-7.0-bin folder
5. copy the path "C:\...\MongoDB\Server\7.0\bin"
6. paste this path into system env variables-path-edit-new-paste_path
7. type mongosh in terminal and it should work

I first pre-processed the data:
1. saved into csv format
2. Experience column, I deleted the 'years' so the column can be integer instead of string
