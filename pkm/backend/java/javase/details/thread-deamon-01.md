- 堂吉诃德（用户线程）：执着于幻想，完成自己的"使命"
- 桑丘（守护线程）：保持现实，守护主人，主人结束他也结束

```java
package ex_thread;  
  
public class DonQuixoteWorld {  
    public static void main(String[] args) throws InterruptedException {  
        System.out.println("=== 拉曼查的冒险开始 ===");
        
        // 堂吉诃德线程（用户线程 - 幻想骑士）
        Thread donQuixote = new Thread(() -> {
            System.out.println("🤠 堂吉诃德骑上驽骍难得，开始冒险！");
            String[] enemies = {"风车巨人", "羊群大军", "酒囊巨人", "理发师的铜盆头盔", "狮子"};
            int sanity = 100;  // 理智值
            
            for(int adventure = 0; adventure < enemies.length; adventure++) {
                System.out.println("\n📖 第" + (adventure+1) + "次冒险：挑战" + enemies[adventure]);
                
                // 每次冒险消耗理智
                int cost = (int)(Math.random() * 30) + 10;
                sanity -= cost;
                
                if(sanity <= 0) {
                    System.out.println("💔 堂吉诃德理智耗尽，回归现实");
                    return;
                }
                
                // 幻想战斗
                if(Math.random() > 0.3) {
                    System.out.println("⚔️ 堂吉诃德击败了" + enemies[adventure] + "！");
                } else {
                    System.out.println("💥 堂吉诃德被" + enemies[adventure] + "打败了");
                }
                System.out.println("理智值剩余: " + sanity);
                
                try {
                    Thread.sleep(1000);  // 冒险间隔
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            System.out.println("\n🏆 堂吉诃德完成所有冒险，成为传奇骑士！");
        }, "堂吉诃德");
        
        // 桑丘线程（守护线程 - 忠实侍从）
        Thread sancho = new Thread(() -> {
            System.out.println("👨‍🌾 桑丘·潘沙骑上灰驴，跟随主人");
            String[] reminders = {
                "老爷，那是风车不是巨人！",
                "小心点，那是羊群不是军队！",
                "您需要吃点东西休息一下",
                "我们回家吧，杜尔西内娅小姐在等您",
                "让我帮您拿着长矛"
            };
            String[] comforts = {
                "给老爷递上水囊",
                "帮老爷整理铠甲",
                "给老爷讲个笑话",
                "提醒老爷注意现实",
                "记录冒险经历"
            };
            
            while(donQuixote.isAlive()) {
                // 随机提醒或安慰
                if(Math.random() > 0.5) {
                    String reminder = reminders[(int)(Math.random() * reminders.length)];
                    System.out.println("🗣️ 桑丘提醒：" + reminder);
                } else {
                    String comfort = comforts[(int)(Math.random() * comforts.length)];
                    System.out.println("🤲 桑丘：" + comfort);
                }
                
                try {
                    Thread.sleep(400);  // 侍从活动间隔
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            System.out.println("🌅 堂吉诃德的冒险结束，桑丘回到家乡");
        }, "桑丘·潘沙");
        
        // 启动冒险
        donQuixote.start();
        Thread.sleep(200);  // 让堂吉诃德先出发
        sancho.start();
        
        // 等待堂吉诃德冒险结束
        donQuixote.join();
        
        System.out.println("\n=== 拉曼查的故事流传后世 ===");
    }
}
```
