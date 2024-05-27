document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.exitButton').forEach(button => {
        button.addEventListener('click', exit);
    });

    document.querySelectorAll('input[type="number"], select').forEach(input => {
        input.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault();
                this.closest('.block').querySelector('button').click();
            }
        });
    });
});

function proceedStep1() {
    const choice = document.getElementById('choice').value;
    if (choice === '1' || choice === '2') {
        document.getElementById('step1').classList.add('hidden');
        if (choice === '1') {
            document.getElementById('budgetInput').classList.remove('hidden');
        } else if (choice === '2') {
            document.getElementById('costInput').classList.remove('hidden');
        }
    }
}

function proceedStep2() {
    const budget = parseFloat(document.getElementById('budget').value);
    const people = parseInt(document.getElementById('people').value);

    if (isNaN(budget) || isNaN(people) || budget <= 0 || people <= 0) {
        document.getElementById('errorBudgetInput').classList.remove('hidden');
    } else {
        document.getElementById('errorBudgetInput').classList.add('hidden');
        document.getElementById('budgetInput').classList.add('hidden');
        document.getElementById('percentages').classList.remove('hidden');
    }
}

function proceedStep2b() {
    const maxCost = parseFloat(document.getElementById('maxCost').value);
    const people = parseInt(document.getElementById('people2').value);

    if (isNaN(maxCost) || isNaN(people) || maxCost <= 0 || people <= 0) {
        document.getElementById('errorCostInput').classList.remove('hidden');
    } else {
        document.getElementById('errorCostInput').classList.add('hidden');
        document.getElementById('costInput').classList.add('hidden');
        document.getElementById('percentages').classList.remove('hidden');
    }
}

function checkPercentages() {
    const aperitivo = parseFloat(document.getElementById('aperitivo').value) || 0;
    const cena = parseFloat(document.getElementById('cena').value) || 0;
    const main = parseFloat(document.getElementById('main').value) || 0;
    const total = aperitivo + cena + main;

    if (total !== 100) {
        document.getElementById('errorPercent').classList.remove('hidden');
    } else {
        document.getElementById('errorPercent').classList.add('hidden');
        document.getElementById('percentages').classList.add('hidden');
        document.getElementById('events').classList.remove('hidden');
    }
}

function calculateCost() {
    const choice = document.getElementById('choice').value;
    const budget = choice === '1' ? parseFloat(document.getElementById('budget').value) : parseFloat(document.getElementById('maxCost').value) * parseInt(document.getElementById('people2').value);
    const people = choice === '1' ? parseInt(document.getElementById('people').value) : parseInt(document.getElementById('people2').value);

    const aperitivo = document.getElementById('aperitivoCheckbox').checked ? parseFloat(document.getElementById('aperitivo').value) || 0 : 0;
    const cena = document.getElementById('cenaCheckbox').checked ? parseFloat(document.getElementById('cena').value) || 0 : 0;
    const main = document.getElementById('mainCheckbox').checked ? parseFloat(document.getElementById('main').value) || 0 : 0;

    const aperitivoCost = (aperitivo / 100) * budget / people;
    const cenaCost = (cena / 100) * budget / people;
    const mainCost = (main / 100) * budget / people;
    const totalCost = aperitivoCost + cenaCost + mainCost;

    document.getElementById('costResults').classList.remove('hidden');
    document.getElementById('costResults').innerHTML = `
        <p>Costo totale per Aperitivo: €${aperitivoCost.toFixed(2)}</p>
        <p>Costo totale per Cena: €${cenaCost.toFixed(2)}</p>
        <p>Costo totale per Main Event: €${mainCost.toFixed(2)}</p>
        <p>Costo totale: €${totalCost.toFixed(2)}</p>
    `;
}

function exit() {
    document.querySelectorAll('.block').forEach(block => {
        block.classList.add('hidden');
    });
    document.getElementById('step1').classList.remove('hidden');
    document.getElementById('choice').value = '';
    document.getElementById('budget').value = '';
    document.getElementById('people').value = '';
    document.getElementById('maxCost').value = '';
    document.getElementById('people2').value = '';
    document.getElementById('aperitivo').value = '';
    document.getElementById('cena').value = '';
    document.getElementById('main').value = '';
    document.getElementById('aperitivoCheckbox').checked = false;
    document.getElementById('cenaCheckbox').checked = false;
    document.getElementById('mainCheckbox').checked = false;
    document.getElementById('errorBudgetInput').classList.add('hidden');
    document.getElementById('errorCostInput').classList.add('hidden');
    document.getElementById('errorPercent').classList.add('hidden');
    document.getElementById('costResults').classList.add('hidden');
}
