import builtins
import unittest

from . import *

class Tests(unittest.TestCase): 

    def setUp(self):

        self.tr = TestRegistrator()
        self.th = self.tr.handler(self)

    def _file(file_name:str):

        def a(f:typing.Callable[['Tests'],None]):

            def test_(self:'Tests'):
    
                f(self)
                builtins.print(f'\nTest file: {file_name}',end=' ')
                self.th.test_file(file_name)

            return test_
        
        return a

    @_file('Test1.java')
    def test_1(self):

        self.tr.r_package       (entity.PackageDeclaration    (name='project.tests.java_files'))
        self.tr.r_import        (entity.ImportDeclaration     (name='java.util.Map'))
        self.tr.r_class         (entity.ClassHeaderDeclaration(name='Test1', header=model.ConcreteClassHeader(access=model.AccessModifiers.PUBLIC)))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='a1'             , attribute=model.Attribute(type=model.Type('int')                 , access=model.AccessModifiers.PRIVATE)))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='a2', static=True, attribute=model.Attribute(type=model.Type('boolean'))))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='a3'             , attribute=model.Attribute(type=model.Type('String', array_dim=1) , access=model.AccessModifiers.PROTECTED)))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='a4', static=True, attribute=model.Attribute(type=model.Type('Object')              , access=model.AccessModifiers.PUBLIC)))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='b1', static=True, attribute=model.Attribute(type=model.Type('int')                 , access=model.AccessModifiers.PRIVATE      , value=' 123'           , final =True)))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='b2'             , attribute=model.Attribute(type=model.Type('boolean')                                                         , value='   true'        , final =True)))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='b3'             , attribute=model.Attribute(type=model.Type('String')              , access=model.AccessModifiers.PROTECTED    , value='  "abc"'        , final =False)))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='b4', static=True, attribute=model.Attribute(type=model.Type('Object', array_dim=2) , access=model.AccessModifiers.PUBLIC       , value=' new Object[]{}', final =True)))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='c1', static=True, attribute=model.Attribute(type=model.Type('Object', array_dim=1) , access=model.AccessModifiers.PUBLIC       , value='null'           , final =True)))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='c2', static=True, attribute=model.Attribute(type=model.Type('Object', array_dim=2) , access=model.AccessModifiers.PUBLIC       , value='null'           , final =True)))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='c3', static=True, attribute=model.Attribute(type=model.Type('Object', array_dim=2) , access=model.AccessModifiers.PUBLIC       , value='null'           , final =True)))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='c4', static=True, attribute=model.Attribute(type=model.Type('Object', array_dim=3) , access=model.AccessModifiers.PUBLIC       , value='null'           , final =True)))
        self.tr.r_attribute     (entity.AttributeDeclaration  (name='c5', static=True, attribute=model.Attribute(type=model.Type('Object', array_dim=4) , access=model.AccessModifiers.PUBLIC       , value='null'           , final =True)))
        self.tr.r_initializer   (entity.InitializerDeclaration(initializer=model.Initializer(body='\n'+8*' '+'System.out.println("Hello");\n'        +4*' '), static=False))
        self.tr.r_initializer   (entity.InitializerDeclaration(initializer=model.Initializer(body='\n'+8*' '+'System.out.println("Hello, static");\n'+4*' '), static=True))
        self.tr.r_constructor   (entity.ConstructorDeclaration(model.Constructor(access=model.AccessModifiers.PUBLIC,  args={'properties':model.Argument(type=model.Type('Map'    , generics=[model.Type(name='String'),model.Type(name='String')])),
                                                                                                                             'awesome'   :model.Argument(type=model.Type('Boolean'))}, body='')))
        self.tr.r_constructor   (entity.ConstructorDeclaration(model.Constructor(access=model.AccessModifiers.PRIVATE, args={'data'      :model.Argument(type=model.Type('byte'   , array_dim=1))}, body=f'\n{8*' '}Test1(null, false);\n{4*' '}')))
        self.tr.r_constructor   (entity.ConstructorDeclaration(model.Constructor(access=model.AccessModifiers.DEFAULT, args={}, body=f'')))
        self.tr.r_class_end     ()

    @_file('Test2.java')
    def test_2(self):

        self.tr.r_package       (entity.PackageDeclaration    (name='project.tests.java_files'))
        self.tr.r_import        (entity.ImportDeclaration     (name='java.util.*'))
        self.tr.r_class         (entity.ClassHeaderDeclaration(name='Test2'                     , header=model.ConcreteClassHeader(access=model.AccessModifiers.PUBLIC)))
        self.tr.r_method        (entity.MethodDeclaration     (name='Test2', method=model.ConcreteMethod(access=model.AccessModifiers.PUBLIC, type=model.Type(name='void'), args={'ints':model.Argument(annotations=[model.Annotation(name='QueryParam')], type=model.Type(name='List', generics=[model.Type(name='Integer', annotations=[model.Annotation(name='NonNull')])]))}, body='')))
        self.tr.r_constructor   (entity.ConstructorDeclaration(model.Constructor(access=model.AccessModifiers.PUBLIC,                                               args={'ints':model.Argument(annotations=[model.Annotation(name='QueryParam')], type=model.Type(name='List', generics=[model.Type(name='Integer', annotations=[model.Annotation(name='NonNull')])]))}, body='')))
        self.tr.r_method        (entity.MethodDeclaration     (name='Test2', method=model.ConcreteMethod(access=model.AccessModifiers.PUBLIC, type=model.Type(name='void'), args={'ints':model.Argument(annotations=[model.Annotation(name='QueryParam'), model.Annotation(name='Foo', args=['"Bar"', '"Baz"'])], type=model.Type(name='List', generics=[model.Type(name='Integer', annotations=[model.Annotation(name='NonNull')])]))}, body='')))
        self.tr.r_class_end     ()
