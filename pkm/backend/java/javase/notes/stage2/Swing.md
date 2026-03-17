# Swing

---

## 入门

* **核心类：`Component`**  提供两个关键绘图方法：  
    1. `paint(Graphics g)`  
       • **功能**：绘制组件的外观（如按钮、窗口等）。  
       • **调用时机**：组件首次显示时自动调用。  
    2. `repaint()`  
       • **功能**：请求刷新组件外观（内部会触发`paint()`）。  
* **`paint()`方法触发场景**  以下三种情况会调用`paint()`：  
    1. **窗口最小化后恢复**  
       • 系统需重新渲染界面内容。  
    2. **窗口大小改变**  
       • 布局调整后需重绘组件。  
    3. **显式调用`repaint()`**  
       • 程序主动请求刷新（如数据更新时）。  
* 将`repaint()`理解为“主动刷新信号”，`paint()`是“实际执行绘画”。  

```java
package demo;  
  
import javax.swing.*;  
import java.awt.*;  
  
public class DrawCircle extends JFrame { // JFrame理解成画框  
    private MyPanel mp;  
    public static void main(String[] args) {  
        new DrawCircle();  
    }    
    public DrawCircle() {  
        mp = new MyPanel();  
        this.add(mp);  
        this.setSize(400,300);  
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  
        this.setVisible(true);  
    }
}  
  
class MyPanel extends JPanel { // JPanel 理解成画纸  
    public void paint(Graphics g) { // Graphics理解画笔  
        super.paint(g);  
        g.drawOval(10, 10, 100, 100);  
    }
}
```

---

## 事件处理

```java
package demo;  

import javax.swing.*;  
import java.awt.*;  
import java.awt.event.KeyEvent;  
import java.awt.event.KeyListener;  

public class BowMove extends JFrame{  
  BowMovePanel panel;  
  public static void main(String[] args) {  
    new BowMove();  
  }    public BowMove() {  
    panel = new BowMovePanel();  
    this.add(panel);  
    this.addKeyListener(panel);  
    this.setTitle("Bow Move");  
    this.setSize(400,300);  
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  
    this.setVisible(true);  
  }
}  

class BowMovePanel extends JPanel implements KeyListener  {  
  public int x;  
  public int y;  

  @Override  
  public void paint(Graphics g) {
    super.paint(g);  
    g.fillOval(x,y,10,10);  
  }
  @Override  
  public void keyTyped(KeyEvent e) {
  }
  @Override  
  public void keyPressed(KeyEvent e) {  
    switch(e.getKeyCode()){  
      case KeyEvent.VK_UP:  
        if(y>10) y-=10;  
        break;  
      case KeyEvent.VK_DOWN:  
        if(y<this.getHeight()-10) y+=10;  
        break;  
      case KeyEvent.VK_LEFT:  
        if(x>10) x-=10;  
        break;  
      case KeyEvent.VK_RIGHT:  
        if(x<this.getWidth()-10) x+=10;  
        break;  
      default:  
        break;  
    }
    this.repaint();  
  }  
  @Override  
  public void keyReleased(KeyEvent e) {
  }
}
```

1. Java事件处理是采取‘委派事件模型’。当事件发生时，产生事件的对象，会把此‘信息’传递给‘事件的监听者’处理，这里所说的‘信息’实际上就是 `java.awt.event` 事件类所创建的对象，把它称为‘事件的对象’。
2. 事件源：事件源是一个产生事件的对象，比如按钮，窗口等。  
3. 事件：事件就是承载事件源状态改变时的对象，比如当键盘事件、鼠标事件、窗口事件  等等，会生成一个事件对象，该对象保存着当前事件很多信息，比如 KeyEvent 对象有含有被按下键的Code值。`java.awt.event` 和 `javax.swing.event` 包中定义了各种事件类型
4. 事件监听器接口：
    1. 当事件源产生一个事件，可以传送给事件监听者处理  
    2. 事件监听者实际上就是一个类，该类实现了某个事件监听器接口 比如前面我们案例中的MyPanle就是一个类，它实现了 KeyListener 接口，它就可以作为一个事件监听者，对接受到的事件进行处理  
    3. 事件监听器接口有多种，不同的事件监听器接口可以监听不同的事件，一个类可以实现多个监听接口这些接口在 java.awt.event 和 javax.swing.event 包中列出常用的事件监听器接口

```java
package demo;  

import javax.swing.*;  
import java.awt.*;  
import java.awt.event.KeyEvent;  
import java.awt.event.KeyListener;  
import java.util.Vector;  

public class DrawTank extends JFrame {  
  GamePanel panel;  
  int width = 1080;  
  int height = 720;  

  public static void main(String[] args){  
    new DrawTank();  
  }  
  public DrawTank(){  
    panel = new GamePanel(width, height);  
    this.add(panel);  
    this.addKeyListener(panel);  
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  
    this.setTitle("Tank");  
    this.setSize(width, height);  
    this.setVisible(true);  
  }
}

class GamePanel extends JPanel implements KeyListener{  
  Hero hero;  
  Vector<Enemy> enemies;  
  public GamePanel(int width, int height){  
    hero = new Hero(width/2, height-60*2, 40, 60, 0, 5);  
    enemies = new Vector<>();  
    for(int i=0; i<3; i++)  
      enemies.add(new Enemy(width/2-60+60*i, 60, 40, 60, 1, 5));  
  }  
  @Override  
  public void paint(Graphics g){  
    super.paint(g);  
    drawBackground(g);  
    drawTank(g, hero);  
    for(Enemy e: enemies)
      drawTank(g, e);  
  }  
  void drawBackground(Graphics g){  
    g.setColor(Color.black);  
    g.fillRect(0, 0, this.getWidth(), this.getHeight());  
  }
  void drawTank(Graphics g, Tank hero){  
    int x = hero.getX();  
    int y = hero.getY();  
    int width = hero.getWidth();  
    int height = hero.getHeight();  
    int direct = hero.getDirection();  
    int type = hero.getType();  
    switch(type){  
      case 0: // 我们的坦克  
        g.setColor(Color.cyan);  
        break;  
      case 1: // 敌人的坦克  
        g.setColor(Color.yellow);  
        break;  
    }        
    switch(direct){  
      case 0: // 向上  
        g.fill3DRect(x, y, (int)(width*0.25), height, false); // 左履带  
        g.fill3DRect(x+(int)(width*0.75), y, (int)(width*0.25), height, false); // 右履带  
        g.fill3DRect(x+(int)(width*0.25), y+(int)(height/6.0), (int)(width*0.50), (int)(height*2.0/3), false); // 车身  
        g.fillOval(x+(int)(width*0.25), y+(int)(height/3.0), (int)(width*0.50), (int)(height/3.0)); // 炮塔底座  
        g.drawLine(x+(int)(width*0.5), y, x+(int)(width*0.5), y+(int)(height/2.0)); // 炮管  
        break;  

      case 1: // 向下  
        g.fill3DRect(x, y, (int)(width*0.25), height, false); // 左履带  
        g.fill3DRect(x+(int)(width*0.75), y, (int)(width*0.25), height, false); // 右履带  
        g.fill3DRect(x+(int)(width*0.25), y+(int)(height/6.0), (int)(width*0.50), (int)(height*2.0/3), false); // 车身  
        g.fillOval(x+(int)(width*0.25), y+(int)(height/3.0), (int)(width*0.50), (int)(height/3.0)); // 炮塔底座  
        g.drawLine(x+(int)(width*0.5), y+(int)(height/2.0), x+(int)(width*0.5), y+height); // 炮管（向下）  
        break;  

      case 2: // 向左  
        g.fill3DRect(x, y, height, (int)(width*0.25), false); // 上履带  
        g.fill3DRect(x, y+(int)(width*0.75), height, (int)(width*0.25), false); // 下履带  
        g.fill3DRect(x+(int)(height/6.0), y+(int)(width*0.25), (int)(height*2.0/3), (int)(width*0.50), false); // 车身  
        g.fillOval(x+(int)(height/3.0), y+(int)(width*0.25), (int)(height/3.0), (int)(width*0.50)); // 炮塔底座  
        g.drawLine(x, y+(int)(width*0.5), x+(int)(height/2.0), y+(int)(width*0.5)); // 炮管（向左）  
        break;  

      case 3: // 向右  
        g.fill3DRect(x, y, height, (int)(width*0.25), false); // 上履带  
        g.fill3DRect(x, y+(int)(width*0.75), height, (int)(width*0.25), false); // 下履带  
        g.fill3DRect(x+(int)(height/6.0), y+(int)(width*0.25), (int)(height*2.0/3), (int)(width*0.50), false); // 车身  
        g.fillOval(x+(int)(height/3.0), y+(int)(width*0.25), (int)(height/3.0), (int)(width*0.50)); // 炮塔底座  
        g.drawLine(x+(int)(height/2.0), y+(int)(width*0.5), x+height, y+(int)(width*0.5)); // 炮管（向右）  
        break;  
    }    
  }  
  @Override  
  public void keyTyped(KeyEvent e) {  

  }  
  @Override  
  public void keyPressed(KeyEvent e) {  
    switch(e.getKeyCode()){  
      case KeyEvent.VK_UP:  
      case KeyEvent.VK_W:  
        hero.setDirection(0);  
        hero.setY(hero.getY()-hero.getSpeed());  
        break;  
      case KeyEvent.VK_DOWN:  
      case KeyEvent.VK_S:  
        hero.setDirection(1);  
        hero.setY(hero.getY()+hero.getSpeed());  
        break;  
      case KeyEvent.VK_LEFT:  
      case KeyEvent.VK_A:  
        hero.setDirection(2);  
        hero.setX(hero.getX()-hero.getSpeed());  
        break;  
      case KeyEvent.VK_RIGHT:  
      case KeyEvent.VK_D:  
        hero.setDirection(3);  
        hero.setX(hero.getX()+hero.getSpeed());  
        break;  
      default:  
        break;  
    }        this.repaint();  
  }  
  @Override  
  public void keyReleased(KeyEvent e) {  

  }
}  

class Tank{  
  private int x;  
  private int y;  
  private int width;  
  private int height;  
  private int direction;  
  private int speed;  
  private int type;  

  public Tank(int x, int y, int width, int height, int direction, int speed, int type) {  
    this.x = x;  
    this.y = y;  
    this.width = width;  
    this.height = height;  
    this.direction = direction;  
    this.speed = speed;  
    this.type = type;  
  }
  public int getX() {  
    return x;  
  }
  public void setX(int x) {  
    this.x = x;  
  }
  public int getY() {  
    return y;  
  }
  public void setY(int y) {  
    this.y = y;  
  }  
  public int getWidth() {  
    return width;  
  }  
  public void setWidth(int width) {  
    this.width = width;  
  }  
  public int getHeight() {  
    return height;  
  }  
  public void setHeight(int height) {  
    this.height = height;  
  }  
  public int getDirection() {  
    return direction;  
  }  
  public void setDirection(int direction) {  
    this.direction = direction;  
  }  
  public int getSpeed() {  
    return speed;  
  }  
  public void setSpeed(int speed) {  
    this.speed = speed;  
  }  
  public int getType() {  
    return type;  
  }  
  public void setType(int type) {  
    this.type = type;  
  }
}  

class Hero extends Tank{  
  public Hero(int x, int y, int width, int height, int direction, int speed) {  
    super(x, y, width, height, direction, speed, 0);  
  }
}  

class Enemy extends Tank{  
  public Enemy(int x, int y, int width, int height, int direction, int speed) {  
    super(x, y, width, height, direction, speed, 1);  
  }
}
```