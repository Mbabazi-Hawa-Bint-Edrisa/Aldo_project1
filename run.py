
import sys
print(sys.path)

from aldo_safaris.init  import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)