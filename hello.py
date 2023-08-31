from java.util import ArrayList  # Importing a Java class
from HelloJava import HelloJava  # Importing a Java class from package

def main():
    print("Hello from Python!")

    # Using Java ArrayList
    java_list = ArrayList()
    java_list.add("Hello")
    java_list.add("World")
    print("Java ArrayList:", java_list)

    # Calling Java program
    HelloJava.main(None)

if __name__ == "__main__":
    main()
