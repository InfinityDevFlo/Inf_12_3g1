from datetime import date


class User(object):

    def __init__(self, id: int, groups: list["Group"], name: str, birth: date, pwhash: str):
        self.name = name
        self.birth = birth
        self.pwhash = pwhash
        self.id = id
        self.groups = groups

    def getName(self) -> str:
        return self.name

    def getBirth(self) -> date:
        return self.birth

    def getGroups(self) -> list["Group"]:
        return self.groups

    def getId(self) -> int:
        return self.id

    def setPawwort(self, pw: str) -> None:
        self.pwhash = hash(pw)

    def addGroup(self, group: "Group") -> bool:
        if group in self.groups:
            return False
        self.groups.append(group)
        return True

    def removeGroup(self, group: "Group") -> bool:
        if group not in self.groups:
            return False
        self.groups.remove(group)
        return True


class Group(object):

    def __init__(self, id: int, name: str, users: list[User], rights: list[str]):
        self.id = id
        self.name = name
        self.users = users
        self.rights = rights

    def getName(self) -> str:
        return self.name

    def getUsers(self) -> list[User]:
        return self.users

    def getId(self) -> int:
        return self.id

    def addUser(self, user: User) -> bool:
        if user not in self.users:
            self.users.append(user)
            return True
        return False

    def removeUser(self, user: User) -> bool:
        if user in self.users:
            self.users.remove(user)
            return True
        return False

    def getRights(self) -> list[str]:
        return self.rights

    def addRight(self, right: str) -> bool:
        if right not in self.rights:
            self.rights.append(right)
            return True
        return False

    def removeRight(self, right: str) -> bool:
        if right in self.rights:
            self.rights.remove(right)
            return True
        return False


class Class(object):

    def __init__(self, name: str, member: list[User], teacher: User):
        self.name = name
        self.member = member
        self.teacher = teacher


    def addMember(self, member: User) -> "Class":
        self.member.append(member)
        return self

    def removeMember(self, member: User) -> "Class":
        self.member.remove(member)
    