from myproject import db


class NumberPlate(db.Model):
    __tablename__ = "number_plate"
    reg_number = db.Column(db.String(64), unique=True, index=True, primary_key=True)
    reg_name = db.Column(db.String(64))
    
    def __init__(self, reg_number, reg_name):
        self.reg_number = reg_number
        self.reg_name = reg_name