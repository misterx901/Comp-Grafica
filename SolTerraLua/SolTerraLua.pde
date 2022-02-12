void setup(){
size(800,800);
}
float velocidade=0;

void draw(){
 
  background(0);
  
  translate(width/2,height/2);
  fill(255, 200, 50);
  circle(0,0,50);
  
  rotate(velocidade);
  translate(140,0);
  fill(50, 200, 255);
  circle(0,0,35);
 
  rotate(velocidade*3);
  translate(45,0);
  fill(255, 255, 255);
  circle(0,0,20);

 velocidade+=0.01;
}
