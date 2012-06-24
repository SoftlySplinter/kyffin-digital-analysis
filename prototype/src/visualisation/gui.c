#include<stdlib.h>
#include<stdio.h>
#include<ctype.h>
#include<unistd.h>
#include<SDL/SDL.h>

#define DEFUALT_WIDTH 640
#define DEFAULT_HEIGHT 480

int running = 0;
int width = DEFUALT_WIDTH; 
int height = DEFAULT_HEIGHT;

void on_event(SDL_Event *event) {
	if(event->type == SDL_QUIT) {
		running = 0;
	}
}

void render() {
	
}

void start_loop(SDL_Surface* surface) {
	SDL_Event event;
	running = 1;

	while(running) {
		while(SDL_PollEvent(&event)) {
			on_event(&event);
		}
	}	
}

int start_gui() {
	SDL_Surface* surface;

	int ret = 0;
	ret = SDL_Init(SDL_INIT_EVERYTHING); 

	if( ret == -1 ) {
		printf("Unable to initialise SDL: %s\n", SDL_GetError());
		return ret;
	}

	surface = SDL_SetVideoMode(width, height, 32, SDL_HWSURFACE | SDL_DOUBLEBUF);

	if(surface == NULL) {
		printf("Unable to create SDL Surgace.\n");
		return -1;
	}

	start_loop(surface);


	return 1;
}

int parse_args(int argc, char** argv) {
	opterr = 0;
	int c = 0;
	while((c=getopt(argc, argv, "w:h:")) != -1) {
		switch(c) {
			case 'w':
				width = atoi(optarg);
				break;
			case 'h':
				height = atoi(optarg);
				break;
			case '?':
				if(optopt == 'w' || optopt == 'h') {
					fprintf(stderr, "Option -%c requires an option.\n", optopt);
				} else if(isprint(optopt)) {
					fprintf(stderr, "Option -%c not recognised.\n", optopt);
				} else {
					fprintf(stderr, "Unknown option character `\\x%x'.\n", optopt);
				}
				return 2;
			default:
				return 2;
		}
	}

	return 0;
}

int main(int argc, char **argv) {
	// TODO: Argument handlling.
	int args = parse_args(argc, argv);

	if( args != 0 ) {
		return args;
	}

	int gui = start_gui();
	if( !gui ) {
		printf("Error starting GUI\n");
		return gui;
	}

	return EXIT_SUCCESS;
}
