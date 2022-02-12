void setup() {
  size(800, 800);
  background(255);
  strokeWeight(5);
  stroke(0);
}
float r=20;
float theta = 0;

void draw() {    
    translate(width/2,height/2);
    float x = r * cos(theta);
    float y = r * sin(theta);
    point(x,y);
    theta+=0.02;
    r+=0.1;
}