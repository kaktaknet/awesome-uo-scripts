using System; 
using Server; 
using Server.Gumps; 
using Server.Network;
using Server.Items;
using Server.Mobiles;

namespace Server.Gumps
{ 
   public class PotionsGump : Gump 
   { 
      public static void Initialize() 
      { 
         Commands.Register( "Pots", AccessLevel.Player, new CommandEventHandler( PotionsGump_OnCommand ) ); 
      } 


      private static void PotionsGump_OnCommand( CommandEventArgs e ) 
      { 
         e.Mobile.SendGump( new PotionsGump( e.Mobile ) ); 
      }
      public PotionsGump( Mobile owner ) : base( 50,50 ) 
      { 
         AddPage( 0 ); 
         AddBackground( 0, 0, 375, 300, 5054 ); 
	 AddLabel( 130, 30, 0, "Potions Menu");
	 AddItem( 200, 175, 3851 );
         AddItem( 200, 225, 3851 );
	 AddItem( 200, 65, 3851 );
         AddItem( 200, 105, 3851 );
	 AddItem( 200, 145, 3851 );

         AddButton( 60, 68, 0x2623, 0x2622, 1, GumpButtonType.Reply, 0 );
	 AddLabel( 85, 65, 1157, "Mana" ); 

         AddButton( 60, 108, 0x2623, 0x2622, 2, GumpButtonType.Reply, 0 );
         AddLabel( 85, 105, 1266, "Stamina" ); 

         AddButton( 60, 148, 0x2623, 0x2622, 3, GumpButtonType.Reply, 0 );
         AddLabel( 85, 145, 33, "Heal" ); 

         AddButton( 60, 188, 0x2623, 0x2622, 4, GumpButtonType.Reply, 0 );
         AddLabel( 85, 185, 1260, "Cure" ); 

         AddButton( 60, 228, 0x2623, 0x2622, 5, GumpButtonType.Reply, 0 );
         AddLabel( 85, 225, 1150, "Night Sight" ); 
}
public override void OnResponse( NetState state, RelayInfo info )
      { 
         Mobile from = state.Mobile; 

         switch ( info.ButtonID ) 
         { 
            case 0: 
            { 

               from.SendMessage( "You do not select anything." );
               break; 
            } 
            case 1: 
            { 
		   

		   {
         	   ManaBag ManaBag = new ManaBag();
	       from.AddToBackpack( ManaBag );
               from.SendMessage( "You have been given mana potions." );
		   }
		  
		   {
		   
		   }
		   break;
            } 
            case 2:  
            { 
		   

		   {

         	    StamBag StamBag = new StamBag();
		   from.AddToBackpack( StamBag );
                   from.SendMessage( "You have been given refresh potions." );
                   }
		   
		   {
		   
		   }
		   break;
            }
            case 3: 
            {
		 
		   {
         	  HealBag HealBag = new HealBag();
		   from.AddToBackpack( HealBag );
                   from.SendMessage( "You have been given healing potions." );
		   }
		  		   
		   {
		   
		   }
		   break;
            } 
            case 4: 
            {   
		  
		   {
         	   CureBag CureBag = new CureBag();
		   from.AddToBackpack( CureBag );
                   from.SendMessage( "You have been given cure potions." );
		   }
		   		   
		   {
		   
		   }
		   break;
            } 
            case 5: 
            { 
		   
		   {
         	   NSBag NSBag = new NSBag();
		   from.AddToBackpack( NSBag );
                   from.SendMessage( "You have been given night sight potions." );

		   }
		   
		   {
		   
		   }
		   break;

            }

	           
}
}
}
}