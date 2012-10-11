package fiji;

import ij.IJ;
import ij.io.FileSaver;
import imagescience.feature.Smoother;
import imagescience.image.ColorImage;
import imagescience.image.Image;

public final class Blur {
	public static final String IMG_PATH = "tux.png";
	public static final String OUTPUT_PATH = "tux_fiji.png";
	
	public static void main(String[] args) {
		final Image image = new ColorImage(IJ.openImage(IMG_PATH));
		final Smoother s = new Smoother();
		final Image blurred = s.gauss(image, 9f);
		final FileSaver fs = new FileSaver(blurred.imageplus());
		fs.saveAsPng(OUTPUT_PATH);
	}
}
