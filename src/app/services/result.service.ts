import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class ResultService {
  queries: any;
  constructor(private http: Http) { }

  getResult(values, startYear, endYear, corpora, smoothing) {
    this.queries = {
      arguments: values,
      startYear: startYear,
      endYear: endYear,
      corpora: corpora,
      smoothing: smoothing
    };
    return this.http.get('./result', { params: this.queries }).map(res => {
      return res.json();
    });
  }
}
