
.PHONY: clean

run_c.exe: main.c
	gcc -o run_c.exe main.c -Wall

clean:
	del run_c.exe
