import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { ResultService } from '../../services/result.service';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {
  public myForm: FormGroup;
  public submitted: Boolean;
  public downloadable;
  public resultLink;
  public events: any[] = [];
  constructor(private resultService: ResultService) { }
  public smoothingArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50];

  public corpora = [{ Name: 'American_English-2012', Value: 17 }, { Name: 'American English-2009', Value: 5 },
  { Name: 'British English-2012', Value: 18 }, { Name: 'British English-2009', Value: 6 },
  { Name: 'Chinese-2012', Value: 23 }, { Name: 'Chinese-2009', Value: 11 },
  { Name: 'English-2012', Value: 15 }, { Name: 'English-2009', Value: 0 },
  { Name: 'English Fiction-2012', Value: 16 },
  { Name: 'English Fiction-2009', Value: 4 },
  { Name: 'English OneMillion-2009', Value: 1 }, { Name: 'French-2012', Value: 19 },
  { Name: 'French-2009', Value: 7 }, { Name: 'German-2012', Value: 20 },
  { Name: 'German-2009', Value: 8 }, { Name: 'Hebrew-2012', Value: 24 },
  { Name: 'Hebew-2009', Value: 9 }, { Name: 'Spanish-2012', Value: 21 },
  { Name: 'Spanish-2009', Value: 10 }, { Name: 'Russian-2012', Value: 25 },
  { Name: 'Russia-2009', Value: 12 }, { Name: 'Italian', Value: 22 }
  ];

  ngOnInit() {
    this.downloadable = true;
    this.myForm = new FormGroup({
      values: new FormControl('', [<any>Validators.required]),
      startYear: new FormControl('', [<any>Validators.required]),
      endYear: new FormControl('', [<any>Validators.required]),
      corpora: new FormControl('', [<any>Validators.required]),
      smoothing: new FormControl('', [<any>Validators.required])
    });
  }

  save(model: any, isValid: Boolean) {

    if (isValid) {
      this.downloadable = true;
      this.submitted = true;
      console.log(model);
      this.resultService.getResult(model.values, model.startYear, model.endYear, model.corpora, model.smoothing).subscribe(result => {
        this.downloadable = false;
        const name = result.fileName;
        this.resultLink = './output/' + name;
      });
    }
  }


}
