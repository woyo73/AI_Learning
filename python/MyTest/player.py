import json


class Player:

    # 초기화
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp   
        self.attack_power = attack_power     

    # 정보 표시 
    def show_info(self):
        print(f"{self.name} : HP {self.hp} : atk power {self.attack_power}")

    # 데미지추가 
    def take_damage(self, damage):
        if damage < 0:
            raise ValueError("damage는 음수일 수 없다.")
        self.hp = max(0, self.hp - damage)

    # 회복
    def heal(self, amount):
        if amount < 0:
            raise ValueError("heal amount 음수일 수 없다.")
        
        self.hp = min(100, self.hp + amount)
        print(f"{amount} 회복 완료!")


    # 세이브
    def save(self, file_name):
        data = {
            "name":  self.name,
            "hp":  self.hp,
            "attack_power":  self.attack_power
        }

        with open(f"{file_name}.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # 로드
    def load(self, file_name):
        with open(f"{file_name}.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            self.name = data["name"]
            self.hp = data["hp"]
            self.attack_power = data["attack_power"]



class Warrior(Player):  
  def power_attack(self):
    return self.attack_power * 2


            
          
        
