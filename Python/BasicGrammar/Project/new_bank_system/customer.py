class Customer:
    def __init__(self,name,id_number) -> None:
        self.name = name
        self.id_number = id_number
    #自定义格式化输出
    def __str__(self) -> str:
        return f"Customer:{self.name} (ID:{self.id_number})"