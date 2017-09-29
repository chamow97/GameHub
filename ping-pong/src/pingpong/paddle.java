package pingpong;

import java.awt.Graphics;

public interface paddle {
	public void draw(Graphics g);
	public void move();
	public int getY();
	
}
