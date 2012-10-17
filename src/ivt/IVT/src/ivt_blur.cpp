#include "Image/ByteImage.h"
#include "Image/ImageProcessor.h"
#include <stdio.h>

int main(int argc, char** argv) {
	if(argc != 2) {
		printf("Expects 2 params\n");
		return 1;
	}
	CByteImage image;
	if(!image.LoadFromFile(argv[0])) {
		printf("Unable to load file %s\n", argv[0]);
		return 2;
	}
	CByteImage out = CByteImage(image);

	ImageProcessor::GaussianSmooth3x3(&image, &out);
	out.SaveToFile(argv[1]);

	return 0;
}
