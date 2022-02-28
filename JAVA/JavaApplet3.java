import java.applet.*;
import java.awt.*;
public class JavaApplet3 extends Applet {
	public void paint(Graphics g) {
		g.drawString("Welcome in the java Applet",100,100);
		showStatus("Showing the status bar message");
	}

}
