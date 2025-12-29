import random


class GiftWheelGame:
    def __init__(self):
        self.players = [] #รายชื่อผู้เล่น
        self.wheel = [] #รายชื่อในวงล้อ
        self.current_player = None #ผู้เล่นปัจจุบัน
        self.results = {} #ผลลัพธ์ของผู้เล่นแต่ละคน เช่น (ผู้เล่นAได้รับของขวัญของB)
        self.started = False #สถานะการเริ่มเกม
        self.frist = True #สถานะการหมุนครั้งแรก
    # --------------------------------------------------------------------------------------------
    # add player to the game
    # เพิ่มผู้เล่นเข้าสู่เกม
    # --------------------------------------------------------------------------------------------

    def add_player(self, player_name):
        # if game started, cannot add player
        # ถ้าเกมเริ่มแล้วจะไม่สามารถเพิ่มผู้เล่นได้
        if self.started:
            return False
        
        # add player and check duplicate
        # เพิ่มผู้เล่นและตรวจสอบการซ้ำกัน
        if player_name and player_name not in self.players:
            self.players.append(player_name)
            return True
        
        return False

    # --------------------------------------------------------------------------------------------
    # start the game
    # เริ่มเกม
    # --------------------------------------------------------------------------------------------
    
    def start_game(self, first_player):
        # if game started, cannot start again
        # ถ้าเกมเริ่มแล้วจะไม่สามารถเริ่มใหม่ได้
        if self.started:
            raise ValueError("Game has already started. เกมได้เริ่มแล้ว")

        # check len of players
        # ตรวจสอบจำนวนผู้เล่น
        if len(self.players) < 2:
            return ValueError("Need at least 2 players to start the game. ต้องมีผู้เล่นอย่างน้อย 2 คนเพื่อเริ่มเกม")

        # check if first player is in players list
        # ตรวจสอบว่าผู้เล่นคนแรกอยู่ในรายชื่อผู้เล่นหรือไม่
        if first_player not in self.players:
            return ValueError("First player must be in the players list. ผู้เล่นคนแรกต้องอยู่ในรายชื่อผู้เล่น")
        
        # set results dict and started status
        # ตั้งค่าผลลัพธ์และสถานะการเริ่มเกม
        self.results = {}
        self.started = True
        self.current_player = first_player

        #  randomize the wheel excluding the first player
        # สุ่มวงล้อโดยไม่รวมผู้เล่นคนแรก
        self.wheel = [player for player in self.players if player != first_player]

    # --------------------------------------------------------------------------------------------
    # spin the wheel for the current player
    # หมุนวงล้อสำหรับผู้เล่นปัจจุบัน
    # --------------------------------------------------------------------------------------------
    def spin_wheel(self):
        if not self.started:
            raise RuntimeError("game has not started yet. เกมยังไม่เริ่ม")
        
        if not self.wheel:
            raise RuntimeError("game is already finished. เกมจบแล้ว")
        
        # choose a randow target from the wheel
        # เลือกของขวัญแบบสุ่มจากวงล้อ
        target = random.choice(self.wheel)

        # record the result and remove the target from the wheel
        # บันทึกผลลัพธ์และลบของขวัญที่ได้รับออกจากวงล้อ
        self.results[self.current_player] = target

        self.wheel.remove(target)
        # update the wheel
        # อัปเดตวงล้อ
        if self.first:
            self.players.append(self.current_player)
            self.first = False
        else:
            self.wheel.remove(target)
        # new player turn
        # เปลี่ยนผู้เล่น
        self.current_player = target

        return target

    # --------------------------------------------------------------------------------------------
    # chack the game this ended or not
    # ตรวจสอบว่าเกมจบหรือไม่
    # --------------------------------------------------------------------------------------------
    def game_is_finished(self):
        pass

    # --------------------------------------------------------------------------------------------
    # result of the game
    # ผลลัพธ์ของเกม
    # --------------------------------------------------------------------------------------------
    def get_results(self):
        pass

    # --------------------------------------------------------------------------------------------
    # reset the game
    # รีเซ็ตเกม
    # --------------------------------------------------------------------------------------------
    def reset_game(self):
        self.__init__()