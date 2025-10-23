'''
#include <iostream>
#include <string>
using namespace std;

class Pokemon {
private:
	int level;
	string name;
public:
	Pokemon(const string& name, int level) : name(name), level(level) {}

	string getName() const {
		return name;
	}
	int getLevel() const {
		return level;
	}
};

ostream& operator<<(ostream& left, const Pokemon& right) {
	left << right.getName() << "(" << right.getLevel() << ")\n";
	return left;
}

int main() {
	Pokemon p1("Pikachu", 5);
	Pokemon p2("Squirtle", 3);

	cout << p1;  // 포켓몬이름(레벨)
	cout << p2;
	return 0;
}
'''

class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    def __str__(self):  # magic method (operator overloading)
        # return "%s(%s)" % (self.name, self.level)
        # return "{}({})".format(self.name, self.level)
        return f"{self.name}({self.level})"

p1 = Pokemon("Pikachu", 5)
p2 = Pokemon("Squirtle", 3)

print(p1)  # cout << p1;
print(p2)
