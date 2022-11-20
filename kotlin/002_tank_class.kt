fun myFun1(){
    for(i in 1..20) println("Ste-$i")
//    var x = 0
//    while(x<20){
//        x++
//        println("Step-$x")
//    }
}

fun myFun2(a: Double,b: Double):Double {
    var c = (b - a)/2 + a
    return c
}

fun myFun3(a: IntArray){ // Max
    var x = a[0]
    for(n in a){
        if(x<n) x = n
    }
    println("Max is: $x")
}

fun myFun3plus(a: IntArray){ // Min
    var x = a[0]
    for(n in a){
        if(x>n) x = n
    }
    println("Min is: $x")
}

class MyTank(var model: String, var color: String, var bullets: Int = 0) {
    var totalDistance = 0

    fun move(d: Int){
        this.totalDistance += d
        println("Tank moved for: $d meters")
    }

    fun turnLeft(){
        println("Turned Left")
    }

    fun turnRight(){
        println("Turned Right")
    }

    fun shot(){
        if(this.bullets > 0){
            println("Baam!")
            this.bullets--
        } else {
            println("Sorry, but you have no bullets.")
        }
    }

    fun getTotalDistance(){
        println("Total distance: ${this.totalDistance}")
    }

    fun getBullets(){
        println("Bullets left: ${this.bullets}")
    }

}

fun main(args: Array<String>) {
//    val test = intArrayOf(2,5,10,1,-3,15)
//    myFun3plus(test)
//    val tank1 = MyTank("T34","green",20)
//    tank1.move(12)
//    tank1.turnRight()
//    tank1.shot()
//    tank1.move(15)
//    tank1.getTotalDistance()
//    tank1.getBullets()

//    print("Enter your name: ")
//    val n = readLine()!!.toInt()
//    println("Hello, $name")
}

