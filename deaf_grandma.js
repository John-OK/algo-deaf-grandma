function deafGrandma() {
    let goodbyes = 0;
    let input = window.prompt('HEY KID!');
    while (goodbyes < 2) {
        if (input == "GOODBYE!") {
            if (goodbyes == 0) {
                input = window.prompt('LEAVING SO SOON?')
                goodbyes++;
            } else {
                window.prompt('LATER, SKATER!')
                goodbyes++;
            }
        }else if (input == "") {
            input = window.prompt('WHAT?!')
        }else if (input != input.toUpperCase()) {
            input = window.prompt('SPEAK UP, KID!')
        }else {
            input = window.prompt('NO, NOT SINCE 1946!')
        }
    }
}

deafGrandma();