fun main(args: Array<String>) {
    /*
    Помогите пожалуйста с кодом этой задачи:
    Сухробу на день рождения подарили n кубиков. Он с друзьями решил построить из них пирамиду.
    Сухроб хочет построить пирамиду следующим образом: на верхушке пирамиды должен находиться 1 кубик,
    на втором уровне 1+2=3 кубика, на третьем 1+2+3=6 кубиков, и так далее. Таким образом, на i-м уровне пирамиды
    должно располагаться 1+2+...+(i-1)+i кубиков.
    Сухроб хочет узнать, пирамиду какой максимальной высоты он может создать с использованием имеющихся кубиков.
    
    Входные данные
    В первой строке записано целое число n (1 <= n >= 104) — количество кубиков, подаренных Сухробу.
    
    Выходные данные
    Выведите единственной строкой максимально возможную высоту пирамиды.
    */
    print("Enter your number: ")
    var n = readLine()!!.toInt()
    var height = 0
    var inlayer = 1
    while (inlayer <= n) {
        height += 1
        n -= inlayer
        inlayer += 1
    }
    println("The height of the pyramid: $height")
}
