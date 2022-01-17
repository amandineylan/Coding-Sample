//From a Food Menu Display project

//library imports
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

//Main Class
public class ComboItem implements Item {
    private final Set<DietaryCategory> aDietaryCategory; /* allow zero or more, does not allow duplications */
    SpecialApplicator aDiscount;
    private ArrayList<Item> aElements = new ArrayList<Item>(); //<Item> is an interface
    private double aPrice;
    private String aName;
    private FoodType aFoodType;

//Object Creation Method
    /**
     * @param pName     the name of the item
     * @param pDiscount the discount factor to apply to the combo
     */
    public ComboItem(String pName, SpecialApplicator pDiscount, FoodType pFoodType, Item... pElements) {
        assert pName != null;
        String itemName = pName.substring(0, 1).toUpperCase() + pName.substring(1).toLowerCase();
        aName = itemName;
        aDietaryCategory = new HashSet<>();
        aPrice = 0;
        aDiscount = pDiscount;
        aFoodType = pFoodType;
        for (Item i : pElements) {
            aElements.add(i);
            aPrice += i.getPrice();
        }


    }

//Functional Method
    /**
     * add an Item to the combo
     *
     * @param pItem the Item to add
     * @pre pItem != null
     */
    public void add(Item pItem) {
        assert pItem != null;
        aElements.add(pItem);
        aPrice += pItem.getPrice();
    }
    
 //Object Data Encapsulation
    /**
	 * @return: the name of the item
	 */
    @Override
    public String getName() {
        return aName;
    }
    
 // Interface
public interface Item {
    /**
     * @return the name of the item
     */
    String getName();

    /**
     * @return the price of the item
     */
    double getPrice();

    /**
     * @return the dietary categories of the item
     */
    Set<DietaryCategory> getDietaryCategory();

    /**
     * @param pDietaryCategory the Dietary Category to set to
     */
    void addDietaryCategory(DietaryCategory pDietaryCategory);

    /**
     * @return the food type of the item
     */
    FoodItem.FoodType getaFoodType();

    /**
     * @param pFoodType the food type to set the item to
     */
    void setaFoodType(FoodItem.FoodType pFoodType);

    /**
     * The types of Food
     */
    enum FoodType {DRINK, SNACK, MAIN}
}

