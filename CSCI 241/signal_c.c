#include <stdio.h>
#include <signal.h>

int window_change = 0;

void my_handler(int sig) // similar to multithreading
{
  (void)sig;
  window_change = 1;
}

int main()
{
  struct sigaction act;
  act.sa_handler = my_handler; // sig. handler function
  sigemptyset(&act.sa_mask); // No other signals blocked
  act.sa_flags = SA_RESTART;// restart signal handling

  sigaction(SIGWINCH, &act, NULL);
  sigaction(SIGINT, &act, NULL); //makes it not possible to exit the program with ^C
  while(1) {
    if(window_change == 1){
      printf("Window size changed!\n");
      window_change = 0;
    }
  }
}
