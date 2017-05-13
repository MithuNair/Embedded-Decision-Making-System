#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc,char *argv[])
{
    	FILE* file;
	char *temp[2] = {"dummy","bye_dummy"};
	char audiofile[23]; 
	int j=1;
	char count[100];
	char tmp[200];
	char tmp1[500];
	int error=-1;
	Py_Initialize();
	//while(1)
	{
		//recording command passing
		//char *temp[2] = {"dummy","bye_dummy"};
		//char audiofile[23];
		//sprintf(tmp, "arecord --device=hw:1,0 -d 3 --format S16_LE --rate 44100 -c1 %d.wav", j);
		//system(tmp);		
		error = system("pwd");
		
		if(error != -1) {
			//dynamic name assignment
			//sprintf(audiofile, "%d.wav", j);	
			//sprintf(audiofile, "195_998.wav",j);
			sprintf(audiofile, "glass.wav",j);
			//sprintf(audiofile, "Explosion+8.wav",j);			
			temp[1] = audiofile;
			//FFT			
	    		Py_SetProgramName(argv[0]);
   			
    			PySys_SetArgv(2, temp);
			file = fopen("/home/pi/ff.py","r");																																		
    			PyRun_SimpleFile(file, "/home/pi/ff.py");
			//printf("hiiiiiiiiiiii");
			fclose(file);
			j++;
		}
			//sprintf(tmp1,"wc -l audio.txt");
			//system(tmp1);
			//printf("Comparison: \n");
		//sprintf(tmp1, "awk 'NR == FNR { x[$1] = $1+0; next; } { for (i in x) { if (x[i] > $1+0 && x[i] < $2+0) { print x[i], $3; } } }' audio.txt sample.txt");
		//system(tmp1);
		
			//sprintf(count,"grep -Rl 'curl' ./ | wc -l");
			//system(count);
			
			//sprintf(count, "nawk '$1>=200 && $1>=900 && c++;END{print c+0}' audio.txt");
			//system(count);
			//if (count>14)
			 //printf ("Explosion sound detected ");
	}	
	Py_Finalize();
	return 0;
}
