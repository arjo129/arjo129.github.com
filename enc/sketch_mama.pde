ParticleSystem ps;
ParticleSystem ps2,ps4, ps5;
iParticleSystem ps3; 
float Frames;
int f =244;
int mode=0;
color texts = color(128,128,2);
void setup() {
  size(640,360);
  ps = new ParticleSystem(new PVector(width/2,height/2));
  ps2 = new ParticleSystem(new PVector(width/2,height/2));
  ps4 = new ParticleSystem(new PVector(width/2,height/2));
  ps5 = new ParticleSystem(new PVector(width/2,height/2));
}

void draw() {
  Frames++;
  noStroke();
  background(0);
  ps.addParticle();
  ps.run();
  ps2.addParticle();
  ps2.run();
   ps4.addParticle();
  ps4.run();
   ps5.addParticle();
  ps5.run();
  if(Frames >500){
    if(Frames==501){
      ps3=new iParticleSystem(new PVector(Frames-1000,height/2));
    }
    if(Frames>502){
      f-= random(-5,5);
      texts = color(f,255-f,2);
      fill(texts);
      textSize(60);
      rectMode(CENTER);
      text("Happy Birthday Mama",Frames-500,height/2);
      ps3.addParticle();
      ps3.run();
       texts = color(f,255-f,2);
       fill(texts);
      text("From Shourjo & Arjo",0,Frames-1000);
    }
  }
  if(Frames>1000){
    textSize(56);
   fill(255);
  text("10th August 2010",140,height/2);
  }
}
void mouseClicked(){
   mode = 1;
}
// A simple Particle class

class Particle {
  PVector location;
  PVector velocity;
  PVector acceleration;
  float lifespan;
  color c;
  Particle(PVector l) {
    acceleration = new PVector(random(-0.05,0.05),random(-0.05,0.05));
    velocity = new PVector(random(-1,1),random(-2,0));
    location = l.get();
    lifespan = 60.0;
    c =  color(random(0,255),random(0,255),random(0,255));
  }

  void run() {
    update();
    display();
  }

  // Method to update location
  void update() {
    velocity.add(acceleration);
    location.add(velocity);
    lifespan -= 1.0;
  }

  // Method to display
  void display() {
    stroke(255,lifespan);
    colorMode(RGB, 100);
  
    fill(c,lifespan);
    ellipse(location.x,location.y,8,8);
  }
  
  // Is the particle still useful?
  boolean isDead() {
    if (lifespan < 0.0) {
      return true;
    } else {
      return false;
    }
  }
}




// A class to describe a group of Particles
// An ArrayList is used to manage the list of Particles 

class ParticleSystem {
  ArrayList<Particle> particles;
  PVector origin;

  ParticleSystem(PVector location) {
    origin = location.get();
    particles = new ArrayList<Particle>();
  }

  void addParticle() {
    particles.add(new Particle(origin));
  }

  void run() {
    for (int i = particles.size()-1; i >= 0; i--) {
      Particle p = particles.get(i);
      p.run();
      if (p.isDead()) {
        particles.remove(i);
      }
    }
    origin.add(new PVector(random(-5,5),random(-5,5)));
  }
}
class iParticleSystem {
  ArrayList<Particle> particles;
  PVector origin;

  iParticleSystem(PVector location) {
    origin = location.get();
    particles = new ArrayList<Particle>();
  }

  void addParticle() {
    particles.add(new Particle(origin));
  }

  void run() {
    for (int i = particles.size()-1; i >= 0; i--) {
      Particle p = particles.get(i);
      p.run();
      if (p.isDead()) {
        particles.remove(i);
      }
    }
    origin = new PVector((Frames-500),height/2);
  }
}
class bParticleSystem {
  ArrayList<Particle> particles;
  PVector origin;

  bParticleSystem(PVector location) {
    origin = location.get();
    particles = new ArrayList<Particle>();
  }

  void addParticle() {
    particles.add(new Particle(origin));
  }

  void run() {
    for (int i = particles.size()-1; i >= 0; i--) {
      Particle p = particles.get(i);
      p.run();
      if (p.isDead()) {
        particles.remove(i);
      }
    }
    origin = new PVector((Frames-500),height/2);
  }
}

