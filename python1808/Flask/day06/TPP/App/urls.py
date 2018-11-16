from App.apis.BannerApi import BannerResource
from App.apis.CinemasApi import CinemasResource
from App.apis.MoviesApi import MoviesResource
from App.apis.PermissionApi import PermissionResource
from App.apis.UserActive import UserActiveResource
from App.apis.UserLogin import LoginResource
from App.apis.UserRegisterApi import RegisterResource
from App.apis.CityApi import CityResource
from App.exts import api


# 路由
api.add_resource(CityResource, '/citys/')
api.add_resource(RegisterResource, '/register/')
api.add_resource(UserActiveResource, '/useractive/')
api.add_resource(LoginResource, '/login/')
api.add_resource(PermissionResource,"/permission/")
api.add_resource(BannerResource,"/banner/")
api.add_resource(MoviesResource,"/movies/")
api.add_resource(CinemasResource,"/cinemas/")




