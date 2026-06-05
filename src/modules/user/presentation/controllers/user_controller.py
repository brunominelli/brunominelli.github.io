from flask import request, jsonify, redirect, url_for
from src.shared.injection.container import Container
from src.modules.user.application.dtos.auth_input_dto import AuthInputDto
from src.modules.user.application.dtos.user_input_dto import UserInputDto

class UserController:
    def __init__(self, container:Container):
        self.user = container.user
    
    def login(self):
        data = request.form.to_dict()

        if not data:
            raise Exception("Invalid JSON")
        
        dto = AuthInputDto(**data)

        token = self.user.auth.execute(dto=dto)

        response = redirect(url_for("site.dashboard_page"))
        response.set_cookie("access_token", token.token, httponly=True,secure=False,samesite="Lax")

        return response

    def logout(self):
        response = redirect(url_for("site.auth_page"))
        response.delete_cookie("access_token")

        return response

    def create(self):
        data = request.json

        if not data:
            raise Exception("Invalid JSON")
        
        dto = UserInputDto(**data)

        self.user.create.execute(dto=dto)

        return jsonify({"message": "Usuário criado com sucesso"}), 201
    
    def read_all(self):
        users = self.user.read_all.execute()

        return jsonify([user.__dict__ for user in users]), 200
    
    def read_by_id(self):
        data = request.json

        if not data:
            raise Exception("Invalid JSON")
        
        user = self.user.read_by_id.execute(user_id=data["user_id"])

        return jsonify(user.__dict__), 200
    
    def read_by_email(self):
        data = request.json

        if not data:
            raise Exception("Invalid JSON")
        
        user = self.user.read_by_email.execute(email=data["email"])

        return jsonify(user.__dict__), 200
    
    def update(self):
        data = request.json
   
        if not data:
            raise Exception("Invalid JSON")
        
        dto = UserInputDto(**data)

        self.user.update.execute(dto=dto)

        return jsonify({"message": "Usuário atualizado com sucesso"}), 200
    
    def delete(self):
        data = request.json

        if not data:
            raise Exception("Invalid JSON")

        self.user.delete.execute(user_id=data["user_id"])

        return jsonify({"message": "Usuário excluído com sucesso"}), 200

