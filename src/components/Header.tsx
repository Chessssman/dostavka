
import React from 'react';
import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <header className="bg-background py-4 px-6 md:px-12">
      <div className="container mx-auto flex justify-between items-center">
        <div className="flex items-center">
          <h1 className="text-2xl font-bold text-primary">+7Доставки</h1>
        </div>
        <nav className="hidden md:flex space-x-6">
          <Link to="/" className="text-foreground hover:text-primary transition-colors">Главная</Link>
          <Link to="#about" className="text-foreground hover:text-primary transition-colors">О боте</Link>
          <Link to="#features" className="text-foreground hover:text-primary transition-colors">Возможности</Link>
          <Link to="#tech" className="text-foreground hover:text-primary transition-colors">Технологии</Link>
        </nav>
        <Button variant="outline" className="hidden md:flex">Связаться с нами</Button>
      </div>
    </header>
  );
};

export default Header;
