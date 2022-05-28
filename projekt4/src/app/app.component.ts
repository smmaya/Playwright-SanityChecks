import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, NgModel, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'projekt4';
  tekstWZmiennej = 'To jest tekst z pola z pliku .ts';
  brands = ['Audi', 'BMW', 'Jeep', 'Toyota', 'Austin', 'Citroen', 'Peugeot']
  osoba: Osoba;
  wiek = [...Array(82).keys()].map(x => x + 18)
  dzienTygodnia = [...Array(7).keys()].map(x => x + 1)
  osobaForm: FormGroup;
  EMAIL = 'email'

  ngOnInit(): void {
    this.osoba = new Osoba();
    this.osoba.imie = 'Tomasz';
    this.osoba.czyStudent = true;
    this.wiek.unshift(null);
    // this.osoba.wiek = 57;
    this.osoba.gender = 'male';
    // this.osoba.dniTygodnia = '';
    // this.osoba.adresEmail = '';
    this.intData();
    this.initForm();
  }

  sendForm(): void {
    console.log('osoba:', this.osoba)
  }

  send() {
    console.log('osoba:', this.osoba)
  }

  imieChanged(imie: NgModel): void {
    console.log('imie model:', imie)
  }

  nazwiskoChanged(nazwisko: NgModel): void {
    console.log('nazwisko model:', nazwisko)
  }

  // export class Osoba {
  //   imie: string;
  //   nazwisko: string;
  //   wiek: number;
  //   czyStudent: boolean;
  //   opis: string;
  //   gender: string;
  //   // dniTygodnia: string;
  //   adresEmail: string;
  // }

  initForm(): void {
    this.osobaForm = new FormGroup({
      imie: new FormControl(null, [Validators.required, Validators.minLength(3)]),
      nazwisko: new FormControl('Kowalski'),
      email: new FormControl(null, [Validators.required, Validators.email]),
      wiek: new FormControl(null, Validators.required),
      czyStudent: new FormControl(null, Validators.required),
      opis: new FormControl(this.osoba.opis),
      gender: new FormControl(true, Validators.required),
      dob: new FormControl(null, Validators.required),
      stanowisko: new FormControl(null, Validators.required)
    })
  }
  intData(): void {
    this.wiek.unshift(null); // dodaje element null na 1 pozycję tablicy this.osoba = new Osoba();
    this.osoba.opis = 'przykladowy opis';
  }

  onSubmit(): void {
    console.log('osobaForm:', this.osobaForm);
    this.osoba.imie = this.osobaForm.value.imie;
    this.osoba.nazwisko = this.osobaForm.value.nazwisko;
    this.osoba.email = this.osobaForm.get('email').value;
    this.osoba.wiek = this.osobaForm.get('wiek').value;
    this.osoba.czyStudent = this.osobaForm.get('czyStudent').value;
    this.osoba.opis = this.osobaForm.get('opis').value;
    this.osoba.gender = this.osobaForm.get('gender').value;
    this.osoba.dob = this.osobaForm.get('dob').value;
    this.osoba.stanowisko = this.osobaForm.get('stanowisko').value;
    console.log('osoba:', this.osoba);
  }
}

export class Osoba {
  imie: string;
  nazwisko: string;
  email: string;
  wiek: number;
  czyStudent: boolean;
  opis: string;
  gender: string;
  dob: string;
  stanowisko: string;
}
