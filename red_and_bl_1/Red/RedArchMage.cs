using System;
using System.Collections;
using Server.Items;
using Server.Targeting;

namespace Server.Mobiles
{
	[CorpseName( "a wizard's body" )]
	public class RedArchMage : BaseCreature
	{
		public override bool ShowFameTitle{ get{ return false; } }
		
		[Constructable]
		public RedArchMage() : base( AIType.AI_Mage, FightMode.Closest, 10, 1, 0.2, 0.4 )

		{			
			SpeechHue = Utility.RandomDyedHue(); 
			Name = "a red archmage"; 
			Hue = Utility.RandomSkinHue(); 
			Body = 0x190; 

 	   		 // *Begin* //
   	   		Item studdedchest = new StuddedChest();
      
         		studdedchest.Hue = 2118;
        		 studdedchest.Movable = false;

        		 AddItem( studdedchest );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item studdedlegs = new StuddedLegs();
      
         		studdedlegs.Hue = 2118;
        		 studdedlegs.Movable = false;

        		 AddItem( studdedlegs );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item studdedarms = new StuddedArms();
      
         		studdedarms.Hue = 2118;
        		 studdedarms.Movable = false;

        		 AddItem( studdedarms );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item studdedgorget = new StuddedGorget();
      
         		studdedgorget.Hue = 2118;
        		 studdedgorget.Movable = false;

        		 AddItem( studdedgorget );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item studdedgloves = new StuddedGloves();
      
         		studdedgloves.Hue = 2118;
        		 studdedgloves.Movable = false;

        		 AddItem( studdedgloves );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item boots = new Boots();
      
         		boots.Hue = 2118;
        		 boots.Movable = false;

        		 AddItem( boots );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item cloak = new Cloak();
      
         		cloak.Hue = 2118;
        		 cloak.Movable = false;

        		 AddItem( cloak );
        		 // *End* //

       			SetStr( 90, 100 );
			SetDex( 90, 105 );
			SetInt( 160, 200 );
			SetHits( 200, 275 );

			SetDamage( 11, 15 );

			SetSkill( SkillName.MagicResist, 90.0, 100.0 );
			SetSkill( SkillName.EvalInt, 100.0, 110.0 );
			SetSkill( SkillName.Magery, 110.0, 120.0 );
			SetSkill( SkillName.Wrestling, 75.0, 80.0 );
			SetSkill( SkillName.Anatomy, 75.0, 80.0 );

			Fame = 10000;
			Karma = -750;

			VirtualArmor = 40;

			Item hair = new Item( Utility.RandomList( 0x203B, 0x2049, 0x2048, 0x204A ) );
			hair.Hue = Utility.RandomNondyedHue();
			hair.Layer = Layer.Hair;
			hair.Movable = false;
			AddItem( hair );


		}
	
		public override void GenerateLoot()
		{
			AddLoot( LootPack.Rich );
			AddLoot( LootPack.LowScrolls );
		}

		public override bool AlwaysMurderer{ get{ return true; } }

		public RedArchMage( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}
