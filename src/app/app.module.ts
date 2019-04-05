import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { Router } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AppComponent } from './app.component';
import { FormComponent } from './sections/form/form.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { ResultService } from './services/result.service';
const ROUTES = [
  { path: '', component: HomeComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    FormComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpModule,
    RouterModule.forRoot(ROUTES)
  ],
  providers: [ResultService],
  bootstrap: [AppComponent]
})
export class AppModule { }
