const charaDict = {
  p : "歩",
  P : "と",
  l : "香",
  L : "成香",
  n : "桂",
  N : "成桂",
  s : "銀",
  S : "成銀",
  g : "金",
  G : "金",
  r : "飛",
  R : "龍",
  b : "角",
  B : "馬",
  k : "王",
  K : "玉",
  _ : "同",
  "!" : "成",
}

const firstDigit = {
  1: "１",
  2: "２",
  3: "３",
  4: "４",
  5: "５",
  6: "６",
  7: "７",
  8: "８",
  9: "９",
}

const secondDigit = {
  1: "一",
  2: "二",
  3: "三",
  4: "四",
  5: "五",
  6: "六",
  7: "七",
  8: "八",
  9: "九",
}

function convert() {
  const inletStr = document.getElementById("inlet").value.normalize("NFKC")
  let result = inletStr
  const outlet = document.getElementById("outlet")
  const fugo = new RegExp("(\\{|\\[)([0-9!pPlLnNsSgGrRbBkK]*?)(\\}|\\])", "g")
  const matches = inletStr.match(fugo)
  for (const m of matches) {
    let val = ""
    if (m.startsWith("{")) {
      val = "▲"
    } else {
      val = "△"
    }
    const length = m.length
    switch (length) {
      case 3:
      case 4:
        val += charaDict._
        val += charaDict[m[1]]
        if (length === 4 && m[2] === "!") {
          val += charaDict["!"] 
        }
        break;

      case 5:
      case 6:
        val += firstDigit[m[1]]
        val += secondDigit[m[2]]
        val += charaDict[m[3]]
        if (length === 6 && m[4] === "!") {
          val += charaDict["!"] 
        }
        break;
    
      default:
        break;
    }
    result = result.replace(m, val)
  }
  outlet.innerText = result
}
