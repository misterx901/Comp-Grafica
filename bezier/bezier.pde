float p1x;
float p1y;
float p2x;
float p2y;

void setup()
{
  size(800,800);
}

void draw()
{
  background(0);
  float px = 200;
  float py = 500;
  float p3x = 700;
  float p3y = 500;
  
  beginShape();
  
  vertex(px, py);
   
  for(float t = 0; t <= 1; t += 0.01)
  {
    float ax = px + t*(p1x-px);
    float bx = p1x + t*(p2x-p1x);
    float cx = p2x + t*(p3x-p2x);
    float dx = ax + t*(bx-ax);
    float ex = bx + t*(cx-bx);
    float fx = dx + t*(ex-dx);
    
    float ay = py + t*(p1y-py);
    float by = p1y + t*(p2y-p1y);
    float cy = p2y + t*(p3y-p2y);
    float dy = ay + t*(by-ay);
    float ey = by + t*(cy-by);
    float fy = dy + t*(ey-dy);
    
    vertex(fx,fy);  
  }
  
   if(mouseButton == RIGHT && mousePressed)
  {
    p1x = mouseX;
    p1y = mouseY;
  }
  if (mouseButton == LEFT && mousePressed)
  {
    p2x = mouseX;
    p2y = mouseY;
  }
  
  vertex(p3x, p3y);
  endShape(CLOSE);
}
